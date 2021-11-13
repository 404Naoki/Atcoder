def main():
  n = int(input())
  a = list(map(int, input().split()))
  x = int(input())

  a_sum = sum(a)
  if a_sum >= x:
    s = 0
    for i in range(n):
      s += a[i]
      if s >= x:
        print(i + 1)
        exit()

  ans = (x // a_sum) * n
  x -= a_sum * (ans // n)
  for v in a:
    x -= v
    ans += 1
    if x < 0:
      print(ans)
      exit()

if __name__ == '__main__':
  main()