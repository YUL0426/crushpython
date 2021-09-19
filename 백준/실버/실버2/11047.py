210919)
n, k = map(int, input().split())
m=[]
#동전을 받을 리스트
cnt=0
#계산횟수를 세기 위한 변수
for i in range(n):
 m.append(int(input()))
 #파라미터로 입력받은 n만큼 리스트에 동전의 종류를 추가한다
for i in range(n-1, -1, -1):
 #가장 큰 화폐의 종류부터 돌면서 계속 작아진다
 if k == 0:
  break
 if m[i] > k:
  continue
 cnt += k//m[i]
 k %= m[i]
print(cnt)



코드)
N, K = map(int, input().split()) 
coin_lst = []
#동전을 받을 리스트
for i in range(N):
    coin_lst.append(int(input()))

count = 0
for i in reversed(range(N)): #그리디를 위한 reverse로 for문돌리기, 50000원부터
    count += K//coin_lst[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
    K = K%coin_lst[i] # K는 동전으로 나눈 나머지로 계속 반복

print(count)
