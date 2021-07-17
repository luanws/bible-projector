from typing import Any, Callable, Dict, List

from src.error.query_filter_not_found import QueryFilterNotFoundError

QueryFilter = Dict[str, Callable[[str], Any]]


def assert_query_filter_found(query_filter: Dict[str, Any], filter_dict: Dict[str, str]):
    query_filter_not_found_list = [
        k for k in filter_dict if not query_filter.__contains__(k)]
    if len(query_filter_not_found_list) > 0:
        raise QueryFilterNotFoundError(query_filter_not_found_list)


def query_filter_to_sql_filter_list(query_filter: QueryFilter, filter_dict: Dict[str, Any]) -> List:
    assert_query_filter_found(query_filter, filter_dict)
    sql_filter_list = [query_filter[k](filter_dict[k]) for k in filter_dict]
    return sql_filter_list
