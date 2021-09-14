*)bronze2

내 풀이)
a = list(map(int,input().split()))
sum = 0

def mayday(a):
 for i in a:
  sum += i
  i += 1
  print(sum)


모범답안)
def solve(a):
    return sum(a)
  
.....
