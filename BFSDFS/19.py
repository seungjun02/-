from itertools import permutations

n = int(input())

array = list(map(int,input().split()))

plus, minus, multiply, divide = map(int,input().split())

operator = ['+'] * plus + ['-'] * minus + ['*'] * multiply + ['/'] * divide

comb = list(set(permutations(operator, n-1)))

min_result = 1e+10
max_result = -1e+10

def divide(a,b):
  if a >= 0:
    return a//b

  elif a < 0:
    return -((-a)//b)




for c in comb:
  total = array[0]
  
  for i in range(len(c)):
    if c[i] == '+':
      total += array[i+1]

    if c[i] == '-':
      total -= array[i+1]

    if c[i] == '*':
      total *= array[i+1]

    if c[i] == '/':
      total = int(total/array[i+1])


  max_result = max(total,max_result)
  min_result = min(total,min_result)
  


print(max_result)
print(min_result)
