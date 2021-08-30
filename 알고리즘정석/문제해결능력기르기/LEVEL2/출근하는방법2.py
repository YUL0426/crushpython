CODE1) 
# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    # 코드를 쓰세요
    if stairs < 0:
        return 0
    elif stairs < 2:  # stairs == possible_steps일때도 1번 가능하니까
        return 1
    return staircase(stairs - possible_steps[0], possible_steps) + staircase(stairs - possible_steps[1], possible_steps) + staircase(stairs - possible_steps[2], possible_steps)  
print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))
