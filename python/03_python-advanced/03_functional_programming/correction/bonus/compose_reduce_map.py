def map_reduce(f_map, f_reduce):
    return compose(lambda y: reduce(f_reduce, y), lambda x: map(f_map, x))
