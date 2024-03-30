#!/usr/bin/env python3
"""
module containing a function tha returns a tuple of size two containing
start and end index
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ function that returns  a tuple of size two containing a start index
        and an end index corresponding to the range of indexes to return in a
        list for those particular pagination parameters.
    """
    y = page * page_size
    x = y - page_size
    index = (x, y)
    return index
