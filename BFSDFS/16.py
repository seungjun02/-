import sys
sys.setrecursionlimit(10000)

from itertools import combinations

n,m = map(int,input().split())

temp = [[0] * m for i in range(n)]

graph = []
void ,wall, virus = [], [], []

for i in range(n):
  data = list(map(int,input().split()))
  graph.append(data)

  for j in range(m):
    if data[j] == 0:
      void.append((i,j))
    if data[j] == 1:
       wall.append((i,j))
    if data[j] == 2:
      virus.append((i,j))

comb = list(combinations(void,3))

result = 0

def dfs(x,y):
  if x<= -1 or x>=n or y<= -1 or y>= m:
    return False

  if temp[x][y] == 0 or temp[x][y] == 2:

    temp[x][y] = 2

    dfs(x-1,y) 
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)

    
    return True
  return False

    
  
for c in comb:

  for i in range(n):
    for j in range(m):
      temp[i][j] = graph[i][j]

  for a,b in c:
    temp[a][b] = 1

  for a,b in virus:
    dfs(a,b)

  count = 0
  
  for vi in range(n):
    for vj in range(m):
      if temp[vi][vj] == 0:
        count += 1


  result = max(result, count)


print(result)
    




