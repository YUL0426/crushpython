CODE1) 
# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    # 코드를 쓰세요
    if stairs < 0:
        return 0
    elif stairs < 2:  # stairs == possible_steps일때도 1번 가능하니까
        return 1
    return staircase(stairs - possible_steps[0], possible_steps) + staircase(stairs - possible_steps[1], possible_steps) + staircase(stairs - possible_steps[2], possible_steps)
    #...
print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))

CODE2) 모범답안
# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    # 계단 높이가 0 이거나 1 이면 올라가는 방법은 한 가지밖에 없다
    number_of_ways = [1, 1]
    
    # 이 변수들을 업데이트 해주며 n 번째 계단을 오르는 방법의 수를 구한다.
    for height in range(2, stairs + 1):
        number_of_ways.append(0)

        for step in possible_steps:
            # 음수 계단 수는 존재하지 않기 때문에 무시합니다
            if height - step >= 0:
                number_of_ways[height] += number_of_ways[height - step]

    return number_of_ways[stairs]
*매번 오를 수 있는 계단 수가 11, 22, 33일 때, staircase(n)를 수학적으로 staircase(n - 1) + staircase(n - 2) + staircase(n - 3)처럼 표현했습니다.
문제의 최적의 답을 구하는데 부분 문제의 최적의 답을 이용할 수 있군요. 이 문제는 최적 부분 구조가 있습니다.
*중복되는 부분 문제가 있는지 확인하기 위해서
staircase(5) = staircase(4) + staircase(3) + staircase(2)
의 경우를 살펴봅시다.
staircase(4),  staircase(3) 와 staircase(2)를 각각 구해야 되죠?
staircase(4)를 구하려면  staircase(3), staircase(2), staircase(1)을 알아야되고요. 계속 부분 문제들을 계속 구하다 보면 중복되는 부분 문제가 생기게 됩니다.

최적 부분 구조과 중복되는 부분 문제가 동시에 있군요.
*Dynamic Programming 접근법을 사용하면 중복되는 부분 문제들을 한 번씩만 계산해주어서 효율적이게 문제를 풀 수 있겠죠?

리스트를 업데이트해주면서 Tabulation 방식으로 !

print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))

=>시간복잡도 : stairs가 n, possible_steps의 길이가 m이라고 할 때, staircase 함수는 n에 비례하는 반복문 안에 m에 비례하는 반복문 하나가 있죠?
그렇기 때문에 이 함수의 시간 복잡도는 O(mn)O(mn)입니다.
