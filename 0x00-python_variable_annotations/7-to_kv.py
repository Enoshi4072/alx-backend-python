#!/usr/bin/env python3

""" A type annotated function using unions """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:

    """ Type annotatated function returning a tuple """
    return (k, v ** 2.0)
