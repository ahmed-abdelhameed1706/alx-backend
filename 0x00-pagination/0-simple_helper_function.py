#!/usr/bin/env python3
"""a simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """simple helper function"""
    end_index: int = page * page_size
    start_index: int = end_index - page_size

    result: Tuple = (start_index, end_index)

    return result
