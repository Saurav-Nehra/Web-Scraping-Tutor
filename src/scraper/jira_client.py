import requests
from urllib.parse import urljoin

from ..utils.logger import get_logger
from ..utils.retry import retry
from ..utils.config import (
    JIRA_BASE_URL,
    JIRA_AUTH_USER,
    JIRA_AUTH_TOKEN,
    MAX_RESULTS
)
from .rate_limiter import handle_rate_limit

logger = get_logger("jira_client")


class JiraClient:
    def __init__(self, base_url=JIRA_BASE_URL, auth_user=JIRA_AUTH_USER, auth_token=JIRA_AUTH_TOKEN):
        self.base_url = base_url
        self.auth = (auth_user, auth_token) if auth_user and auth_token else None
        self.session = requests.Session()

        if self.auth:
            self.session.auth = self.auth

        self.max_results = MAX_RESULTS

    @retry(Exception, tries=4, backoff_factor=2.0, logger=logger)
    def search_issues(self, jql, start_at=0):
        url = urljoin(self.base_url, "/rest/api/2/search")
        params = {
            "jql": jql,
            "startAt": start_at,
            "maxResults": self.max_results,
            "expand": "renderedFields,changelog",
        }

        resp = self.session.get(url, params=params, timeout=30)

        if resp.status_code == 429:
            handle_rate_limit(resp)
            raise Exception("Rate limited")

        if resp.status_code >= 500:
            logger.warning(f"Server error {resp.status_code}")
            resp.raise_for_status()

        if resp.status_code != 200:
            logger.error(f"Unexpected status code: {resp.status_code} - {resp.text}")
            resp.raise_for_status()

        return resp.json()

    @retry(Exception, tries=4, backoff_factor=2.0, logger=logger)
    def get_comments(self, issue_key):
        url = urljoin(self.base_url, f"/rest/api/2/issue/{issue_key}/comment")
        resp = self.session.get(url, timeout=30)

        if resp.status_code == 429:
            handle_rate_limit(resp)
            raise Exception("Rate limited")

        resp.raise_for_status()
        return resp.json()
