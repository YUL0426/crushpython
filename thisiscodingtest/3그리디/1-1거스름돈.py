n=1260
#그리디로 구해야하는 총 합
count=0
#총 동전 개수 합을 구하기 위한 변수 count
list=[500, 100, 50, 10]
#동전의 총 네가지 종류
for coin in list:
#그리디 구하기 위한 for 문
  count += n // coin
#n을 coin으로 나눈 몫
  n %= coin
#coin으로 나눈 나머지는 다시 n
print(count)
