import time
import random
from functools import wraps




def retry(exceptions, tries=5, backoff_factor=1.5, logger=None):
def decorator(func):
@wraps(func)
def wrapper(*args, **kwargs):
_tries = tries
delay = 1.0
while _tries > 1:
try:
return func(*args, **kwargs)
except exceptions as e:
if logger:
logger.warning(f"{func.__name__} failed with {e}, retrying in {delay:.1f}s...")
time.sleep(delay + random.random() * 0.1)
_tries -= 1
delay *= backoff_factor
return func(*args, **kwargs)
return wrapper
return decorator
