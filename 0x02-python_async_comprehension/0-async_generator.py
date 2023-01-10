#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times,
each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
Using the random module."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """
    coroutine that executes ten times yields a random value 0-10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        random_value = random.uniform(0, 10)
        yield random_value
