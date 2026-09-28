# AB-100 service-case workshop

Start with the [lab instructions](../../docs/labs/ab-100.md). Run from the repository root:

```console
python labs/ab-100/release_gate.py
python -m unittest discover -s labs/ab-100 -v
```

The starter should be blocked; the 13 gate/arithmetic tests should pass. All records are synthetic. `release_gate.py` is a teaching reference, not a trusted evidence producer or a deployable release pipeline. No service is called.
