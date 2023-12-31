#!/usr/bin/env python3
"""
This module Contaains Function
Function arg1: page, arg2:page_size
Return a tuple
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Page numbers are 1-indexed, i.e. the first page is page 1.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: Start index and end index for the given pagination parameters.
    """
    start_index = (page - 1) * (page_size)
    end_index = start_index + page_size

    return start_index, end_index
