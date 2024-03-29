#!/usr/bin/env python3
""" Creating a co-routine """
import asyncio
import random


async def async_generator():
    """ Looping 10 times """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
