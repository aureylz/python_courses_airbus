def my_map(l,f):
    def my_map_len(input_list, len_input_list, f):
        if len_input_list == 0:
            return []
        else:
            return [f(input_list[0])]+my_map_len(input_list[1:], len_input_list-1, f)
    return my_map_len(l, len(l), f)