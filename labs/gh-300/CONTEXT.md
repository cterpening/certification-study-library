# Shipping change context packet

This is an exercise input to copy into a disposable workspace/session. It is not an automatically enforced repository policy.

## Requirement

`shipping_cents(subtotal)` accepts only nonnegative integer cents. Booleans, floats, strings, nulls, collections, and negative integers raise `ValueError`. Shipping is 499 cents below 5,000 cents and zero at or above 5,000 cents. Tax, currency conversion, discounts, external APIs, and UI work are out of scope.

## Relevant files and evidence

- `starter.py`: candidate to fix.
- `test_contract.py`: requirement-derived oracle; do not change the expected values to match a broken implementation.
- At `4999`, expect `499`; at `5000` and `5001`, expect `0`.
- Run `python test_contract.py --implementation starter` inside this lab directory, or the full path command documented in the lab from the repository root.
- Inspect the diff and describe why it fixes the threshold without broadening accepted input types.

## Two session prompts

For the deliberately vague comparison: “Fix the shipping calculation in starter.py.”

For a fresh session with this packet: “Use the requirement and acceptance cases in CONTEXT.md to diagnose starter.py. Propose the smallest justified change. Run the contract suite for starter, report the actual result, and explain the boundary and boolean behavior. Keep unrelated files unchanged.”

The same oracle is used for both sessions. Record the actual client/model, selected context, prompts, patch, commands, output, and review effort. Do not copy an answer from `reference.py` into a session while claiming the model derived it independently. One task is a learning exercise, not evidence of general productivity improvement.
