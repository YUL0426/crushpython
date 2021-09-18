틀린코드)
1)
while True:
 n,m = map(int, input().split())
 print(n + m)
 if n == 0 and m == 0:
  break
2)
while True:
 n,m = map(int, input().split())
 print(n + m)
 if (n == 0 and m == 0):
  break

맞은 내 코드)
while True:
 n,m = map(int, input().split())
 if (n == 0 and m == 0):
  break
 else:
  print(n + m)


모범답안)
while(1):
 a, b = map(int, input().split())
 if (a==0 and b==0):
  break;
 else:
  print(a+b)
