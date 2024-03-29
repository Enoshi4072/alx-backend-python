#!/usr/bin/env python3
""" A type annotated function that returns a float """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Takes a list of floats and returns the sum as a float """
    return float(sum(input_list))
