def main():
  n, a, b = map(int, input().split())

  ans = 0
  for i in range(1, n + 1):
    l = [int(x) for x in list(str(i))]
    if a <= sum(l) <= b:
      ans += i

  print(ans)

if __name__ == '__main__':
  main()