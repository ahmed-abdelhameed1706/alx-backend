#!/usr/bin/env python3
"""a simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    end_index = page * page_size
    start_index = end_index - page_size

    result = (start_index, end_index)

    return result
