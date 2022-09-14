def factorial_reduce(n):
    fac = lambda n: reduce(lambda x, y: x*y, range(1, n+1), 1)
    return fac(n)