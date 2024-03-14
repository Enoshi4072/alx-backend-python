#!/usr/bin/env python3
""" Using sequences, any and union """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:

    """ Augumenting with duct-typed annotations """
    if lst:
        return lst[0]
    else:
        return None
