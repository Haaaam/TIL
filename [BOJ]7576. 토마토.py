from collections import deque

m,n=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
queue=deque()
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0:
                    graph[nx][ny]=graph[x][y]+1
                    queue.append((nx,ny))
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            queue.append((i,j))

bfs()
day=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            print(-1)
            exit()
        if day<graph[i][j]:
            day=graph[i][j]

print(day-1)


















