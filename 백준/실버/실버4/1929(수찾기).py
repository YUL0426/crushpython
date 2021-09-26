분류)
이진탐색

코드)
import sys

def binary_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

m = int(input())
x = list(map(int, sys.stdin.readline().split()))

for k in range(m):
    print(binary_search(a, x[k]))
