from typing import List


class QueryFilterNotFoundError(Exception):
    def __init__(self, query_filter_list: List[str], *args) -> None:
        self.query_filter_list = query_filter_list
        super().__init__(*args)
