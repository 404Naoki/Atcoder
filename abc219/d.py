def main():
  n = int(input())
  x, y = map(int, input().split())
  box = []
  for _ in range(n):
    a, b = map(int, input().split())
    box.append((a, b))

  dp = [[[301] * x] * y)] * (n + 1)


  dp = [[301] * x] * y
  dp[0][0] = 0

if __name__ == '__main__':
  main()
