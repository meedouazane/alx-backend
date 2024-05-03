#!/usr/bin/env python3
""" Simple helper function """


def index_range(page, page_size):
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
