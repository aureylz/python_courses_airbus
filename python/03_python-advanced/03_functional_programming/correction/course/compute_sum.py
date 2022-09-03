def compute_sum(n):
    if n <= 1:
        return n
    return n+compute_sum(n-2)
    