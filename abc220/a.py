def main():
  a, b, c = map(int, input().split())
  for x in range(a, b + 1):
    if x % c == 0:
      print(x)
      exit()

  print(-1)

if __name__ == '__main__':
  main()