# Web-Scrapping-Tutor

This project implements a scalable and fault-tolerant pipeline for scraping public Apache Jira issues and converting them into structured JSONL datasets suitable for Large Language Model (LLM) training.

The system is designed to demonstrate data collection, cleaning, transformation, and task generation in a clear and maintainable architecture.

## Project Overview

The pipeline performs the following steps:

1. Scrapes issues, comments, and metadata from Apache Jira.
2. Handles pagination, retries, rate limits, and malformed data.
3. Saves raw responses in the data/raw directory.
4. Converts raw JSON into a clean JSONL dataset in data/processed.
5. Generates simple derived tasks such as summarization.

The design follows modular principles and separates scraping, transformation, and utility logic for clarity and extensibility.

## Features

1. Resilient scraper with retry mechanisms and exponential backoff.
2. Handles HTTP 429 and server-side errors gracefully.
3. Auto-resume support using a persistent state file.
4. HTML-to-text cleaning for Jira issue fields.
5. Conversion from raw JSON pages to JSONL.
6. Additional task-generation step to create input-output pairs.
7. Organized multi-module architecture.

## Project Structure

Web-Scrapping-Tutor/
├── README.md
├── run.py
├── requirements.txt
├── .gitignore
├── .env.example
├── src/
│   ├── scraper/
│   │   ├── jira_client.py
│   │   ├── issue_scraper.py
│   │   ├── state_manager.py
│   │   └── rate_limiter.py
│   ├── transform/
│   │   ├── jsonl_converter.py
│   │   ├── cleaner.py
│   │   └── task_generator.py
│   └── utils/
│       ├── logger.py
│       ├── retry.py
│       └── config.py
├── data/
│   ├── raw/
│   └── processed/
├── tests/
│   └── test_basic.py
└── docs/
    └── architecture.md

## How to Run the Pipeline

1. Clone the repository.
2. Copy the file `.env.example` to `.env` and adjust values if needed.
3. Create and activate a virtual environment.
4. Install dependencies using `pip install -r requirements.txt`.
5. Run the pipeline using one of the following commands:

   - Scrape only:
     python run.py --step scrape

   - Convert raw data to JSONL:
     python run.py --step convert

   - Generate derived tasks:
     python run.py --step tasks

   - Run all steps:
     python run.py --step all

## Notes

- The scraper uses only publicly available Jira endpoints.
- Raw JSON files are stored in the `data/raw` directory.
- Processed JSONL files are stored in `data/processed`.
- You can extend the project by adding task types, improving text cleaning, or parallelizing the scraper.
