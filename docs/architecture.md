# Architecture

## Overview
This repository contains a small pipeline to scrape public issues from Apache Jira,
store raw JSON pages, convert them into a structured JSONL corpus and generate
simple derived training tasks (e.g., summarization).

## Components
- `src/scraper/` - Jira REST client + orchestration for pagination, rate limiting and state persistence.
- `src/transform/` - Clean raw JSON into `jira_corpus.jsonl` and create derived tasks.
- `src/utils/` - Configuration loading, logging and retry helpers.
- `data/raw/` - Raw downloaded pages (one JSON file per page).
- `data/processed/` - Final JSONL artifacts for LLM training.
- `tests/` - Minimal unit tests.

## Resilience & Fault Tolerance
- Retry decorator with exponential backoff for transient errors.
- 429 handling using `Retry-After` header.
- `state.json` (via StateManager) to store `startAt` per project for resuming downloads.
- Save raw pages to `data/raw/` so failed transforms can be retried without re-downloading.

## Future improvements
- Parallelize per-project scraping.
- Switch to `httpx` + `asyncio` for higher throughput.
- Add schema validation (pydantic) and richer derived tasks (QA, classification).
