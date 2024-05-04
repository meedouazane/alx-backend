#!/usr/bin/env python3
""" Simple pagination """
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate start index and an end index
    :param page: page number
    :param page_size: size of the pages
    :return: tuple with start and end page
    """
    start_page = (page - 1) * page_size
    end_page = (start_page + page_size)
    tpl = (start_page, end_page)
    return tpl


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
        """
            Get specific page in dataset
            :param page: page number
            :param page_size: size of the pages
            :return: the appropriate page of the dataset
            """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        pages = []
        start, end = index_range(page, page_size)
        if self.dataset():
            pages = self.dataset()[start:end]
        return pages

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        :param page: page number
        :param page_size: size of the pages
        :return: dictionary with specific key-value
        """
        total_page = len(self.dataset()) / page_size
        next_page = page + 1
        prev_page = page - 1
        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page if next_page < total_page else None,
            "prev_page": prev_page if prev_page != 0 else None,
            "total_page": math.ceil(total_page)
        }
