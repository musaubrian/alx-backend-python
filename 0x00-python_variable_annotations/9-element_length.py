#!/usr/bin/env python3
"""Annotate the following code

>>>def element_length(lst):
>>>   return [(i, len(i)) for i in lst]
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return element length
    """
    return [(i, len(i)) for i in lst]
