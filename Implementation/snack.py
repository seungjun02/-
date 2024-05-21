n = int(input())
array = [[0] * (n+1) for _ in range(n+1)]
present = [[0] * (n+1) for _ in range(n+1)]


k = int(input())
for i in range(k):
  r, c = map(int,input().split())
  array[r][c] = 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direction = 1



def rotate_left():
    global direction 
    direction -= 1
    if direction == -1:
        direction = 3

def rotate_right():
    global direction 
    direction += 1
    if direction == 4:
        direction = 0



q = []
x = 1
y = 1


q.append((x,y))
present[x][y] = 1

time = 0

time_array = [0] * 10001


l = int(input())
for i in range(l):
  t, d = input().split()
  if d == 'L':
    time_array[int(t)] = -1
  elif d == 'D':
    time_array[int(t)] = 1




while True:
  time += 1

  nx = x + dx[direction]
  ny = y + dy[direction]

  if nx > n or nx <= 0 or ny > n or ny <= 0 or present[nx][ny]==1:
    break
  
  else:
    x = nx
    y = ny
    present[x][y] = 1
    q.append((x,y))

    if array[x][y] == 0:
      tx,ty = q.pop(0)
      present[tx][ty] = 0
    elif array[x][y] == 1:
      array[x][y] = 0      
 
  if time_array[time] == -1:
    rotate_left()
  elif time_array[time] == 1:
    rotate_right()
  
    
print(time)

    
  
