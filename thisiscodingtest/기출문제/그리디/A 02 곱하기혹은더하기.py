# 맞출 수 있었는데 아쉽다(close)

data = input()

result = int(data[0]) # 첫 번째 문자를 숫자로 변경하여 대입
# 내 오답
result = 0 # 반환할 가장 큰 수 출력을 위한 변수

for i in range(1, len(data)):
    num = int(data[i])              # 먼저 data[i]에 관하여 정의 해주었어야함
    if num <= 1 or result <=1:
        result += num
    else:
        result *= num
#    if data[i] == 0:
#        result += data[i]
#    else:
#        result *= data[i]

print(result)
