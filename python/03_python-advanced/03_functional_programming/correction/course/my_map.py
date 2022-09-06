from typing import List, Iterable
def my_map(list_: List, function)->List:
    def my_map_len(input_list, len_input_list, function):
        if len_input_list == 0:
            return []
        else:
            return [function(input_list[0])]+my_map_len(input_list[1:], len_input_list-1, function)
    return my_map_len(list_, len(list_), function)

