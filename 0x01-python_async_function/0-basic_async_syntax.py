#!/usr/bin/env python3
"""Basic syntax of the async/await"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    delays for a random amount of seconds between 0 and set delay
    Args::
        max_delay(int): the set maximum delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
