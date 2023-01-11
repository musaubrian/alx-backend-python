#!/usr/bin/env python3
"""
The coroutine will collect 10 random numbers
using an async comprehensing over async_generator,
then return the 10 random numbers.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    return 10 numbers from the results of async_generator
    """
    rand_ints = [i async for i in async_generator()]
    return rand_ints
