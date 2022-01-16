s = input()

letter = []
sum = 0

# 문자를 하나씩 확인하며
for i in s:
    # 알파벳인 경우 결과 리스트에 삽입
    if i.isalpha():
        letter.append(i)
    # 숫자는 따로 더하기
    else:
        sum += int(i)

# 알파벳을 오름차순으로 정렬
letter.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if sum != 0:
    letter.append(str(sum))

# 최종 결과 출력
print(''.join(letter))
