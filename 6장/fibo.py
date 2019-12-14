#  피보너치를 처리하는 모듈입니다. 

def fib(n):                         ## 피보너치 함수를 호출하면 결과 값을 출력합니다. 
    a, b = 0, 1
    while a <= n:                  ## 반복을 조건식이 만족할 때까지 처리한다.
        print(a, end=' ')         ##  값을 한 라인에 출력하기 위해  end="" 로 지정해서 개행문자를 빈 문자열로 만듭니다.
        a, b = b, a+b              ## 피보너치 계산을 하기위해 로직을 처리합니다
    print()

def fib2(n):                       ##  피보너치 함수를 호출하면 ㄹreturn Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a <= n:
        result.append(a)
        a, b = b, a+b
    return result
