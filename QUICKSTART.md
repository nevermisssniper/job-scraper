# Access / Jobs — runnable workbench

Filter a sample opportunity board, save listings and export a shortlist.

## Open the interface

Python 3.10+; no npm install, API keys, model download or GPU required for the demo.

```sh
python serve_demo.py
```

Open <http://127.0.0.1:8000>. To use another port: `python serve_demo.py --port 8001`.
Serve `demo/` over HTTP rather than opening `index.html` as a file. The server binds only to localhost.

## What is implemented

The default command imports fictional example listings, normalizes URLs and persists seen IDs in SQLite. A repeat run returns no new listings. Unknown education is never classified as no-degree. Older scraping/LLM/email modules remain historical code and are not imported by the new entry point. Live adapters, credentials and sending are not enabled.

Interface capabilities: Education filters, Saved shortlist, Persistent ingestion.

## Core workflow

From the repository root (install the project's existing dependencies first for model-backed commands):

```sh
python main.py --input examples/jobs.json --database jobs.sqlite3 --education no-degree --output shortlist.json
```

## Verify

The browser's calculation tests use Node 18+ and no third-party packages:

```sh
node --test demo/core.test.cjs
python -m pytest tests/test_pipeline.py -q
```

The GitHub demo workflow checks browser calculations and the dependency-free core tests where present. Full original model/service suites have separate dependencies; passing demo checks does not certify GPU training or external services.

## Before live use

Live sources need explicit adapters and source-specific validation; unknown education stays unknown.

Local browser data belongs to this browser profile. Export records before clearing it or changing devices. Photo previews stay in memory; exported briefs contain filenames, not uploaded image bytes. There are no payment or outbound model calls in this demo.

## Provenance

Workbench and starter additions: AI-assisted implementation, 2026-11-13, for Ray's review. Existing repository history and upstream attribution are preserved. New starter directions are proposals where the GitHub repository had no code.
