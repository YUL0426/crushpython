분류)
1차원 배열

코드)
arr = []

for i in range(9):
    arr.append(int(input()))

print(max(arr))
print(arr.index(max(arr))+1)

*append로 숫자를 받을 때 append(int(input())해야 하는점
*max후 arr[i]가 아니라, arr / 한마디로 그냥 배열명을 치면 된다.
*index를 활용하여 배열위치 찾기                        
