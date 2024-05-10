n ,m = map(int,input().split())

weight = list(map(int, input().split()))

count = 0

weight.sort()

for i in range(len(weight)):
  for j in range(i+1, len(weight)):
    if weight[i] != weight[j]:
      count += 1

print(count)
