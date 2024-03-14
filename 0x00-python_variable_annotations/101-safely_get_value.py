#!/usr/bin/env python3
""" Using Typevar, mapping, Any, Union """
from typing import TypeVar, Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: T = None) -> Union[Any, T]:

    """ Implementing the function """
    if key in dct:
        return dct[key]
    else:
        return default