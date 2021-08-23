def fib_optimized(n):
# 코드를 작성하세요.
 sum = 0
 if n < 3:
 # basecase
  sum = 1
 else:
  fib_optimized(n) = fib_optimized(n - 1) + fib_optimized(n - 2)
  return sum

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))


##########

def fib_optimized(n):
    current = 1
    previous = 0

    # 반복적으로 위 변수들을 업데이트한다. 
    for i in range(1, n):
        current, previous = current + previous, current

    # n번재 피보나치 수를 리턴한다. 
    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
