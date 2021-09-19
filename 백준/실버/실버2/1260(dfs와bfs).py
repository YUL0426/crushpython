

210920코드) 아직 잘 모르겠음
n, m, v = map(int, input().split())
matrix=[[0]*(n+1) for i in range(n+1)]

for i in range(m):
	#무슨 for문인지 모르겠다
	a,b = map(int,input().split())
	matrix[a][b] = matrix[b][a]=1
visited_list=[0]*(n+1)

def dfs(v):
	visited_list[v]=1
	#방문한 점 1로 표치
	print(v, end=' ')
	for i in range(1, n+1):
		if(visited_list[i]==0 and matrix[v][i]==1):
			dfs(i)

def bfs(v):
	queue=[v]
	#들려야할 정점
	visited_list[v]=0
	while queue:
		v=queue.pop(0)
		print(v, end=' ')
		for i in range(1, n+1):
			if(visited_list[i]==1 and matrix[v][i] ==1):
				queue.append(i)
				visited_list[i]=0

dfs(v)
print()
bfs(v)

