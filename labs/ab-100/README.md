# AB-100 service-case workshop

This is an AI-generated, best-effort teaching lab. Its synthetic Python checks
passed locally, but the proposed assistant workflow has not been tested in a real
service or tenant or independently reviewed.

Start with the [lab instructions](../../docs/labs/ab-100.md). Run from the repository root:

```console
python labs/ab-100/release_gate.py
python -m unittest discover -s labs/ab-100 -v
```

The starter should be blocked; the 13 gate/arithmetic tests should pass. All records are synthetic. `release_gate.py` is a teaching reference, not a trusted evidence producer or a deployable release pipeline. No service is called.
