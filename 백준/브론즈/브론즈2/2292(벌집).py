분류)수학적 사고

코드)
n = int(input())
cnt = 1
count = 1
six = 6

while n > cnt:
    count += 1
    #1번방은 무조건 통과하므로
    cnt += six
    #벌집 6개씩 숫자를 계속더해주는데
    six += 6
    #벌집이 커질수록 6이 한번 더키지니까 6도한번 더 더해줘야 한다.
    

print(count)

*six변수를 전혀 생각하지 못했다. 벌집이 커지면서 숫자도6개씩이 아니라 6의배수씩 커지는데 그 부분을 어떻게 해결해야될지에 대한 수학적 사고가 부족하였다.
