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
