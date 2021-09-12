내코드) return outside function오류 발생
n = int(input())
sum=0
i=1

while sum <= n:
    sum += i
    i += 1
    return i
#  
모범답안)
sum=0
i=0
n = int(input())

while True:
    i+=1
    sum+=i
    if(sum>=n):
        print(i)
        break
return이 아니라 print로 i값을 반환해야하지 않았나
잘한점
변수설정동일
못한점
너무복잡하게 while문을 짠 것
