#!/usr/bin/env python3
"""a simple pagination"""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """simple helper function"""
    end_index: int = page * page_size
    start_index: int = end_index - page_size

    result: Tuple = (start_index, end_index)

    return result


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """method to get page"""
        assert isinstance(page, int), "page number must be int"
        assert isinstance(page_size, int), "page size must be int"
        assert page > 0, "page must be possitive"
        assert page_size > 0, "page size must be possitive"

        ds_page = index_range(page, page_size)

        self.dataset()

        if ds_page[0] >= len(self.__dataset):
            return []

        result = [self.__dataset[i] for i in range(ds_page[0], ds_page[1])]

        return result

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """method to return a dict"""
        self.dataset()
        result = {"page_size": page_size, "page": page}

        data = self.get_page(page, page_size)

        result["data"] = data

        total_pages = len(self.__dataset) // page_size

        next_page = page + 1 if total_pages > page else None
        prev_page = page - 1 if page > 1 else None

        result["total_pages"] = total_pages
        result["next_page"] = next_page
        result["prev_page"] = prev_page

        return result
