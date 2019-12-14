
import functools as fs

def decorator_2(func) :
    @fs.wraps(func)                                       ## 전달된 실행함수의 메타정보를 내부함수의 메타정보로 변경한다
    def inner(*args, **kwargs) :
        return func(*args, **kwargs)
    return inner
