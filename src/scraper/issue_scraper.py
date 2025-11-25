import os
import json
from tqdm import tqdm
from pathlib import Path
from .jira_client import JiraClient
from .state_manager import StateManager
from ..utils.config import PROJECTS, RAW_DIR, MAX_RESULTS
from ..utils.logger import get_logger


logger = get_logger('issue_scraper')


class IssueScraper:
def __init__(self, projects=None):
self.client = JiraClient()
self.state = StateManager()
self.projects = projects or PROJECTS


def _save_raw(self, project, start_at, payload):
Path(RAW_DIR).mkdir(parents=True, exist_ok=True)
filename = Path(RAW_DIR) / f'{project}_{start_at}.json'
with filename.open('w', encoding='utf-8') as f:
json.dump(payload, f, indent=2)


def scrape_project(self, project):
logger.info(f"Start scraping project: {project}")
st = self.state.get(project)
start_at = st.get('startAt', 0)
jql = f'project = {project} ORDER BY created ASC'
total = None
pbar = None
while True:
logger.info(f"Fetching {project} startAt={start_at}")
data = self.client.search_issues(jql, start_at=start_at)
if not data or 'issues' not in data:
logger.warning('Empty or malformed data received')
break
issues = data.get('issues', [])
if total is None:
total = data.get('total', None)
pbar = tqdm(total=total, desc=f'{project}') if total else None
self._save_raw(project, start_at, data)
count = len(issues)
start_at += count
if pbar:
pbar.update(count)
# save state
self.state.set(project, {'startAt': start_at})
if count < MAX_RESULTS:
break
if pbar:
pbar.close()
logger.info(f"Finished scraping project: {project}")


def scrape_all(self):
for p in self.projects:
try:
self.scrape_project(p.strip())
except Exception as e:
logger.exception(f"Failed scraping {p}: {e}")


if __name__ == '__main__':
IssueScraper().scrape_all()
