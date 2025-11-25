from pathlib import Path
from dotenv import load_dotenv
import os


load_dotenv()


JIRA_BASE_URL = os.getenv('JIRA_BASE_URL', 'https://issues.apache.org/jira')
JIRA_AUTH_USER = os.getenv('JIRA_AUTH_USER')
JIRA_AUTH_TOKEN = os.getenv('JIRA_AUTH_TOKEN')
PROJECTS = os.getenv('PROJECTS', 'HADOOP,HIVE,SPARK').split(',')
MAX_RESULTS = int(os.getenv('MAX_RESULTS', '100'))
OUTPUT_DIR = os.getenv('OUTPUT_DIR', 'data/processed')
RAW_DIR = os.getenv('RAW_DIR', 'data/raw')
STATE_FILE = os.getenv('STATE_FILE', 'state.json')


Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(RAW_DIR).mkdir(parents=True, exist_ok=True)
