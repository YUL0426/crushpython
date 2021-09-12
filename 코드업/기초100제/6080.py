내코드)
n = int(input())
m = int(input())

for i in range(1, n+1):
 for j in range(1, m+1):
  print(i,j)

#for문을 돌며 i,j는 알아서 증가한다
#n,m입력을 저렇게 받으면..... 공백을 기준으로 입력받는게아니기 때문에 n, m = map(int,input().split())으로 입력하여야함

모범답안)
n,m = map(int,input().split())
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i, j)
