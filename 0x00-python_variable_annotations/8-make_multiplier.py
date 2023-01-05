#!/usr/bin/env python3
"""Returns a function that multiplies a float"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], [float]]:
    """
    Return a function that multiplies an arg by itself
    """
    def multiply(n: float) -> float:
        """
        multiply a n by multiplier
        Args::
            n(float)
        """
        return n*n

    return multiply
