def map_reduce(f_map, f_reduce):
       return lambda x: my_reduce_list((my_map(x, len(x),f_map)),f_reduce,None)