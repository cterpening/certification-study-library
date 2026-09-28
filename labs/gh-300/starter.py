"""Deliberate boundary defect for the learner to diagnose."""


def shipping_cents(subtotal):
    if type(subtotal) is not int or subtotal < 0:
        raise ValueError("subtotal must be a nonnegative integer number of cents")
    return 0 if subtotal > 5000 else 499
