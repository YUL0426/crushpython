분류) 재귀
문제) 팩토리얼

210918코드)
n = int(input())
mul = 1

while n > 0:
 if n == 0:
  print(1)
 else:
  mul = mul * n
  n = n-1
print(mul)


코드)
def fac(n):
 if n <= 1:
  return 1
 else:
  return n*fac(n-1)

print(fac(int(input())))

#파라미터로 n을받으면 된다
#c언어와 다르게 먼저 scanf와같은걸로 입력받는게 아니라, 마지막 print부분에서 int(input)으로 수를 입력받는다.
#재귀의 기본 공식!!!
