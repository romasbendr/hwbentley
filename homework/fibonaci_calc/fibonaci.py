def get_nth_member(n: int) -> int:
    """Calculates and returns nth member of Fibonacci 
    series for n>0"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_nth_member(n-1) + get_nth_member(n-2)
