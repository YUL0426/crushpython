n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))
## for를 활용하여 빈 배열의 리스트를 만들어 append할 필요 없음

#list = []

#for i in range(n):
#    num = int(input(()))
#    list.append(num)

data.sort() ## 입력받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수 , 정렬한 배열크기에서 맨뒤
second = data[n - 2] # 두 번째로 큰 수, 정렬한 배열크기 -2

result = 0

while True:
    for i in range(k): #가장 큰 수를 K번 더하기
        if m == 0: # 숫자가 더해지는 횟수가 0 이라면, 바로 반복문 탈출
            break
        result += first
        m -= 1 # *더할때마다 더해지는 횟수 감소
    if m == 0:
        break
    result += second
    m -= 1 #더할 때마다 1씩 빼기

print(result)

