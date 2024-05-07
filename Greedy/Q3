string = input()


Len_zeros = 0
Len_ones = 0



for i in range(len(string)-1):
  if int(string[i]) != int(string[i+1]):
    if int(string[i]) == 0:
      Len_zeros += 1
    else:
      Len_ones += 1


if int(string[-1]) == 0:
  Len_zeros += 1
else:
  Len_ones += 1

if Len_zeros >= Len_ones:
  print(Len_ones)
else:
  print(Len_zeros)
