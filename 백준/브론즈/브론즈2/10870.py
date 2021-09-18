분류) 재귀
문제) 피보나치 수 5

code)
def fib(num):
    if num <= 1:
        return num
    return fib(num - 1) + fib(num - 2)

print(fib(int(input())))
