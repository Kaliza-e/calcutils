"""Core arithmetic and statistical helper functions for calcutils."""

from typing import Sequence


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def average(numbers: Sequence[float]) -> float:
    """Return the arithmetic mean, or 0.0 when the sequence is empty."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)