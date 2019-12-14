
def decorator_20(func) :
    def inner(*args, **kwargs) :
        return func(*args, **kwargs)
    return inner
