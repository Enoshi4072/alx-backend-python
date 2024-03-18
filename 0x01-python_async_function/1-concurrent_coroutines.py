#!/usr/bin/env python3
""" Executing multiple co-routines """
import asyncio
from typing import List

wait_ran = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Executing wait random n times """
    de_times = []
    for _ in range(n):
        de_time = await wait_ran(max_delay)
        de_times.append(de_time)
    return sorted(de_times)
