#현재 나이트의 위치, 문자열과 숫자가 함께 입력받아지므로 map함수 사용 불가
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) = int(ord('a')) + 1 #여기가 제일이자 유일하게 이해 안감

#나이트가 이동할 수 있는 8가지 방향 정의
steps = [
    (-2,-1), (-1,-2), (1,-2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

#8가지 방향에 대하여 각 위치로 이동 가능한지 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    #해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
