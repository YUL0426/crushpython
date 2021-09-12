잘못된 풀이1)
n= int(input())

for i in range(1, n+1):
 if i % 3 == 0:
  print("X")
 else:
  print(i)

=> 한 줄 출력이 안됨.

잘못된 풀이2)
a = int(input())

for i in range(1, a + 1):

    if (i % 3==0):
        print('X', end=' ')
        continue

    print(i, end=' ')
 
=>29같은수는 걸러낼 수 없음

모범답안)
a = int(input())

for i in range(1, a + 1):

    if (i % 10 == 3 or i % 10 == 6 or i % 10 == 9):
        print('X', end=' ')
        continue

    print(i, end=' ')
    
#end=' '를 활용한 한줄 출력
