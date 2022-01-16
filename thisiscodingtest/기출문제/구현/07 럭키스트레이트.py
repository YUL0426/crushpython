score = input()
length = len(score) # 총 자리수
result = 0

# 왼쪽 부분의 자릿수 합 더하기:
for i in range(length //2):
    result += int(score[i])
#for i in range(1, len(score)):
 #   if len(score)/ 2 ==0:
  #      half =

# 오른쪽 부분의 자릿수 합 뺴기
for i in range(length//2, length):
    result  -= int(score[i])

if result ==0:
    print('LUCKY')
else:
    print('READY')
