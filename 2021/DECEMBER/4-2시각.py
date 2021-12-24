n = int(input())

count = 0               //경우의수를 세기 위해 필요한 변수

for i in range(n+1):    // n가지만 for문을 돌리면 n전까지만(00시) for문이 돌기 때문에
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):       // *** 문자열로 처리하여 3이들어있나 확인한다.
                count +=1

print(count)
