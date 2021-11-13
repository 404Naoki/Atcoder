def main():
  k = int(input())
  a, b = input().split()

  a = a[::-1]
  b = b[::-1]
  a_x = 0
  p = 1
  for x in a:
    a_x += int(x) * p
    p *= k

  b_x = 0
  p = 1
  for x in b:
    b_x += int(x) * p
    p *= k

  print(a_x * b_x)

if __name__ == '__main__':
  main()