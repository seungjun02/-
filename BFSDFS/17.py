from collections import deque

n, k = map(int, input().split())

graph = []

queue = deque()

t = 0

for i in range(n):
  data = list(map(int,input().split()))
  graph.append(data)
  
s,a,b = map(int,input().split())

for v in range(1,k+1):
  for i in range(n):
    for j in range(n):
      if graph[i][j] == v:
        queue.append((i,j,v,t))





dx = [-1 ,1 ,0 ,0]
dy = [0, 0, -1, 1]


while queue:
  x, y, v, t= queue.popleft()

  t += 1

  if t == s+1:
    break
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
      continue

    if graph[nx][ny] == 0:
      graph[nx][ny] = v
      queue.append((nx,ny,v,t))



print(graph[a-1][b-1])

    
      

    
      

  
