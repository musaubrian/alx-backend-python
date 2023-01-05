#!/usr/bin/env python3
"""Type annonate using TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""

from types import NoneType
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, NoneType]) -> Union[Any, T]:
    """
    Args::
        dct(Mapping)
        key(Any)
    """
    
    if key in dct:
        return dct[key]
    else:
        return default
