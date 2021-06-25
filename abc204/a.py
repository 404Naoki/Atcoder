x, y = map(int, input().split())

if x == y:
  print(x)
elif (x == 1 or x == 2) and (y == 1 or y == 2):
  print(0)
elif (x == 0 or x == 2) and (y == 0 or y == 2):
  print(1)
elif (x == 0 or x == 1) and (y == 0 or y == 1):
  print(2)