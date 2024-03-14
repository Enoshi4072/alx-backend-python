#!/usr/bin/env python3
""" Using callables """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    """ Takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier. """
    def mult_func(val: float) -> float:
        return val * multiplier
    return mult_func
