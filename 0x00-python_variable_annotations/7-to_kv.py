#!/usr/bin/env python3
"""Return a Tuple from two arguments"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a k,v Tuple
    Args::
        k(str)
        v(int or float)
    """
    return (k, v**2)
