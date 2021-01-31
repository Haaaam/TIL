from collections import deque
m,n,h=map(int,input().split())
graph=[[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        graph[i].append(list(map(int,input().split())))

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
queue=deque()

def bfs():
    while queue:
        x,y,z=queue.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if graph[nz][nx][ny]==0:
                    graph[nz][nx][ny]=graph[z][x][y]+1
                    queue.append((nx,ny,nz))
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==1:
                queue.append((j,k,i))

bfs()
day=0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==0:
                print(-1)
                exit()
            if day<graph[i][j][k]:
                day=graph[i][j][k]
print(day-1)


