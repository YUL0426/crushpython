#이중 for문 활용
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    #현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a) #리스트에서 가장 작은 원소를 찾아주는 min()함수
    result = max(result, min_value)
        
print(result)
