#!/usr/bin/env python3
"""correct duck-typed annotations of

def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
"""

from types import NoneType
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """
    Return lst or None
    Args::
        lst
    """
    if lst:
        return lst[0]
    else:
        return None
