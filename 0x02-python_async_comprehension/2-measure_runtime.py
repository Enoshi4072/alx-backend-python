#!/usr/bin/env python3
""" Measuring time for synchronousity """
import asyncio
import typing
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Using parallelism """
    start = perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = perf_counter()
    total = end - start
    return total
