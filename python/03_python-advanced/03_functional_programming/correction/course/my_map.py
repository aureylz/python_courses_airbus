from typing import List, Iterable
def my_map(list_: List, len_list: int, function)->List:
    if len_list == 0:
        return []
    else:
        return [function(list_[0])]+my_map(list_[1:], len_list-1, function)
def my_map_iterable(iterable: Iterable, function)->Iterable:
    for item in iterable:
        yield function(item)

