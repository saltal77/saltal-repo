def factorial(n):
    """
    calculates math factorial n!
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    result = 1 # 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()