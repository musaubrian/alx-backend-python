#!/usr/bin/env python3
"""
The code is nearly identical to wait_n
except task_wait_random is being called.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    runs a function mulitple times(n) with delays(max_delay)

    Args::
        n(int): number of times to call the async function
        max_delay(int): amount of delay between function calls
    """
    delays = []
    active_tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(active_tasks):
        delay = await task
        delays.append(delay)
    return delays
