# AI-103 maintenance-assistant contracts

Follow the [lab instructions](../../docs/labs/ai-103.md). From the repository root:

```console
python labs/ai-103/maintenance.py
python -m unittest discover -s labs/ai-103 -v
```

Expected: five retrieval results, a reconciled timeout with one destination record, and 13 passing tests. Read the expected results before the reference implementation. These are synthetic local contracts, with no Azure SDK, model, authentication, or durable storage.
