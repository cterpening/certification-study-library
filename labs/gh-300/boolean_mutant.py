"""Deliberate type-validation defect; bool is an int subclass in Python."""


def shipping_cents(subtotal):
    if not isinstance(subtotal, int) or subtotal < 0:
        raise ValueError("subtotal must be a nonnegative integer number of cents")
    return 0 if subtotal >= 5000 else 499
