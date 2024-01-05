n, m = map(int, input().split())
d_pre = 0

for _i in range(n):
  d_pa = d_pre
  data = list(map(int, input().split()))
  data.sort() 
  d_pre= data[0]
  if d_pre > d_pa:
    result = d_pre

#최대 최소값만 필요할 경우? 정렬하지 말고 min,max 함수 사용하기(값 비교, 리스트에 사용가능)

print(result)



####################

result = 0

for i in range(n):
  data = list(map(int, input().split()))

  m_value = min(data)
  result = max(m_value, result)

print(result)

