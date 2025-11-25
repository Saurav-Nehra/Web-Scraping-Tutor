import argparse
from src.scraper.issue_scraper import IssueScraper
from src.transform.jsonl_converter import convert_all
from src.transform.task_generator import generate_tasks
from src.utils.config import OUTPUT_DIR
from pathlib import Path

def main(args):
    if args.step in ('scrape', 'all'):
        IssueScraper().scrape_all()

    if args.step in ('convert', 'all'):
        out = convert_all()
        print('Wrote:', out)

    if args.step in ('tasks', 'all'):
        jsonl = Path(OUTPUT_DIR) / 'jira_corpus.jsonl'
        if jsonl.exists():
            generate_tasks(jsonl)
            print('Tasks file created beside:', jsonl)
        else:
            print('Processed jsonl not found:', jsonl)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--step', choices=['scrape','convert','tasks','all'], default='all')
    args = p.parse_args()
    main(args)
