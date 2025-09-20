from data_unsorted_a_lot import numbers
from random import randrange

nearly = sorted(numbers)
length = len(nearly)

for i in range(length):
  mix_i = i + randrange(100)
  if mix_i >= length: mix_i -= 100
  nearly[i], nearly[mix_i] = nearly[mix_i], nearly[i]

if __name__ == '__main__':
  print('[')
  for i in range(0, length, 10):
    print('  ', end='')
    e = min(length, i+10)
    for x in range(i, e):
      print(f'{nearly[x]:7d}, ', end='')
    print()
  print(']')