#!/usr/bin/env python3
"""Returns sum of a mixed array"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns sum of a mixed List
    Args::
        mxd_lst(int, float)
    """
    return float(sum(mxd_lst))
