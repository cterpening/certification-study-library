# GH-300 boundary and context workshop

Read the [lab instructions](../../docs/labs/gh-300.md) and `CONTEXT.md` before inspecting the reference. From the repository root:

```console
python labs/gh-300/compare.py
python -m unittest discover -s labs/gh-300 -v
```

Both commands should exit zero on the original files. The comparison verifies that the broken starter fails at exactly 5000, the boolean mutant fails for `True`/`False`, and the reference passes. The unit command tests the reference's seven requirements. Repair a copy of the starter and run `test_contract.py --implementation starter` against that copy. All candidates are AI-assisted teaching examples; no Copilot interaction has been recorded.
