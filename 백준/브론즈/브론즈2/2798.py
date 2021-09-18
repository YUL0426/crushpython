블랙잭

코드)
n, m = map(int, input().split())
#n만큼 리스트를 받기 위해서는 리스트로 받는다
arr = list(map(int, input().split()))
result = 0

#3개의 숫자를 뽑으므로 3중 for
for i in range(n):
 for j in range(i+1, n):
  for k in range(j+1, n):
   if arr[i] + arr[j] + arr[k] > m:
    continue
   else:
    result = max(result, arr[i]+arr[j]+arr[k])

print(result)
