문제)
영훈이는 출근할 때 계단을 통해 사무실로 가는데요. 급할 때는 두 계단씩 올라가고 여유 있을 때는 한 계단씩 올라 갑니다.

어느 날 문득, 호기심이 생겼습니다. 한 계단 또는 두 계단씩 올라가서 끝까지 올라가는 방법은 총 몇 가지가 있을까요?

계단 4개를 올라간다고 가정하면, 이런 방법들이 있습니다.

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
총 5개 방법이 있네요.

함수 staircase는 파라미터로 계단 수 n을 받고, 올라갈 수 있는 방법의 수를 효율적으로 찾아서 리턴합니다.

print(staircase(0))  # => 1
print(staircase(1))  # => 1
print(staircase(4))  # => 5

코드1) 런타임이 오래걸리지만 결과는 나오는,,,
def staircase(n):
    # 코드를 작성하세요.
    if (n <= 1):
        return 1
    return staircase(n-1) + staircase(n-2)
# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))

코드2)
def staircase(n):
    # 코드를 작성하세요.
    case = [1]
    for i in range(1, n+1):
        if i < 2:
            case.append(1)
        else:
            case.append(case[i-1] + case[i - 2])
    return case[n]
# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))

모범답안)
def staircase(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
함수 staircase에는 파라미터 n에 비례하는 반복문 하나가 있습니다. 따라서 이 함수의 시간 복잡도는 O(n)입니다.
