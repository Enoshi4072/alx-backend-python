#!/usr/bin/env python3

""" Executing multiple co-routines """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Executing wait random n times """
    de_times = []
    for _ in range(n):
        de_time = await task_wait_random(max_delay)
        de_times.append(de_time)
    return sorted(de_times)
