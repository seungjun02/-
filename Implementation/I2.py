input_data = input()

### 파이썬 내장함수 ord를 통해 알파벳 순서를 출력 가능
data_x = int(input_data[1])
data_y = int(ord(input_data[0])) - int(ord('a')) + 1 
#문자열 인덱스 사용하기

count = 0


moves = [
  (-2,1),
  (-2,-1),
  (2,1),
  (2,-1),
  (1,-2),
  (1,2),
  (-1,-2),
  (-1,2)
]

for move in moves:
  dx = move[0]
  dy = move[1]

  nx = data_x + dx
  ny = data_y + dy

  if nx < 1 or ny < 1 or nx > 8 or ny > 8:
    continue

  count += 1


print(count)

