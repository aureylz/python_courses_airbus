def my_reduce(l, f, initializer):
    if len(l) == 0:
        return initializer
    if len(l) == 1:
        if initializer is None:
            return None
        else:
            return f(initializer, l[0])
    if initializer is None:
        return my_reduce(l[2:], f, f(l[0], l[1]))
    else:
        return my_reduce(l[1:], f, f(initializer, l[0]))
