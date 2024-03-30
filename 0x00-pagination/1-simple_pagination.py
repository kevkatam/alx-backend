#!/usr/bin/env python3
"""
module containing class Server
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ function that returns  a tuple of size two containing a start index
        and an end index corresponding to the range of indexes to return in a
        list for those particular pagination parameters.
    """
    y = page * page_size
    x = y - page_size
    index = (x, y)
    return index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """  find the correct indexes to paginate the dataset correctly
             and return the appropriate page of the dataset
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        data = self.dataset()

        try:
            indexes = index_range(page, page_size)
            return data[indexes[0]:indexes[1]]
        except IndexError:
            return []
