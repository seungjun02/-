from itertools import combinations

n, m = map(int, input().split())

temp = [[0] * m for _ in range(n)]

graph = []
void, virus = [], []

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

    for j in range(m):
        if data[j] == 0:
            void.append((i, j))
        elif data[j] == 2:
            virus.append((i, j))

comb = list(combinations(void, 3))

result = 0

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if temp[x][y] == 0:
        temp[x][y] = 2

  
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False



for c in comb:
    for i in range(n):
        for j in range(m):
            temp[i][j] = graph[i][j]

    for a, b in c:
        temp[a][b] = 1

    
    for va, vb in virus:
        dfs(va-1, vb)
        dfs(va+1, vb)
        dfs(va, vb+1)
        dfs(va, vb-1)


    

    


    count = 0

    for vi in range(n):
        for vj in range(m):
            if temp[vi][vj] == 0:
                count += 1

    result = max(result, count)

    
    



print(result)
