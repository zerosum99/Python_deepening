def foo(x):
    """
    >>> foo(5)
    5
    """
    return x

if __name__ in ("__main__", "__console__"):
    import doctest
    doctest.testmod(verbose=True)
