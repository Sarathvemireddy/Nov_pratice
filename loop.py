for i in range(5):
  for j in range(5-i):
    print(' ', end='')
  for j in range(i+1):
    print('*', end='')
  print()

for i in range(4, -1, -1):
  for j in range(5-i):
    print(' ', end='')
  for j in range(i+1):
    print('*', end='')
  print()