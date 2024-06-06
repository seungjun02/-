from collections import deque

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)

min_distance = [0] * (n+1)

for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)


def bfs(graph, start, visited):
  queue = deque([start])

  visited[start] = True

  distance = 0
  min_distance[start] = distance
  
  while queue:
    v = queue.popleft()
    distance = min_distance[v] + 1
    
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        min_distance[i] = distance


  count = 0
  
  for i in range(len(min_distance)):
    if min_distance[i] == k:
      print(i)
      count += 1 

  if count == 0:
    print(-1)

bfs(graph,x,visited)
