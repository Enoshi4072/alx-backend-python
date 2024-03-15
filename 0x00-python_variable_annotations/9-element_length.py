#!/usr/bin/env python3
""" Using Sequence, iterables, Tuples, List """
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns values with theor appropriate types """
    return [(i, len(i)) for i in lst]
