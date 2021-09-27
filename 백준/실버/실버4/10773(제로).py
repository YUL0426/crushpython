분류) 정렬

코드) error : list index out of range
k= int(input())
sum = 0
money = []

for i in range(k):
    money.append(int(input()))
    if money[i] == 0:
        del(money[i-1])
for j in range(len(money)):
    #리스트의 길이만큼 for문을 돌면서
    sum += money[j]
    #남아있는 리스트의 값들을 모두 더한다
print(sum)

모범답안)
k= int(input())
money = []

for i in range(k):
    num = int(input())
    if (num == 0):
        money.pop()
    else:
        money.append(num)
print(sum(money))


*if문으로 예외를 먼저 없애는 걸 생각하는건 어떨까?
*입력을 받고 그다음에 그냥 append로 리스트에 넣어줄 수도 있다.
