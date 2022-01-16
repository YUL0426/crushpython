n = int(input())
data = list(map(int, input().split()))
data.sort()     ## 모험도 오름차순 정렬

result = 0 # 반환시킬 총 그룹의 수
count = 0 # 그룹 인원 수

for i in data:
  count += 1 ## 그룹에 인원추가
  if count >= i: ## 인원이 공포도 보다 높으면 팀 결성
    result += 1
    count = 0

print(result)
