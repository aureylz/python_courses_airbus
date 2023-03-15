from functools import reduce


def compose_list(*func):
    def compose(f, g):
        return lambda x: f(g(x))

    return reduce(compose, func)
