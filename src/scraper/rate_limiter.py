import time
from ..utils.logger import get_logger


logger = get_logger('rate_limiter')




def handle_rate_limit(response):
# If Jira returned Retry-After header, obey it
retry_after = response.headers.get('Retry-After')
if retry_after:
try:
wait = int(retry_after)
except ValueError:
wait = 60
else:
wait = 60
logger.warning(f"Rate limited. Sleeping for {wait} seconds")
time.sleep(wait)
