#!/usr/bin/env python3
"""
measure the total runtime and return it.
"""

import asyncio

import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = time.time()
    running_task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*running_task)
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken
