#!/usr/bin/env python3
""" Basics of async """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Uses the random and await method to find the delay time """
    de_time = random.uniform(0, max_delay)
    await asyncio.sleep(de_time)
    return de_time
