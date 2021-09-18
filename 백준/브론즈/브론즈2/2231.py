분류) 브루트 포스

코드)
n = int(input())
result = 0

for i in range(1, n+1):
 a = list(map(int, str(i)))
 #리스트를 통해 i의 각 자릿수를 a리스트에 넣는다
 result = i + sum(a)
 #분해합이 256(245+2+4+5)이므로 문제에 제시된 대로 그대로인 값 i와 각 자리수가 들어간 리스트 a 리스트 값의 합을 더하면 된다
 if result == n:
  print(i)
  break

 if i==n:
  print(0)
  #생성자가 없을경우 0 출
