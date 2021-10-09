def main():
  from itertools import accumulate

  n = int(input())
  a = list(map(int, input().split()))

  cumsum = list(accumulate(a))

  mx = -1
  s = 0
  for i in range(n):
    mx = max(mx, a[i])
    s += cumsum[i]
    print(s + mx * (i + 1))

if __name__ == '__main__':
  main()