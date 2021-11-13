MOD = 998244353

def main():
  n = int(input())
  a = list(map(int, input().split()))

  dp = [[0] * 10] * n
  dp[0][(a[0] + a[1]) % 10] = 1
  dp[0][(a[0] * a[1]) % 10] = 1
  for i in range(n - 2):
    x = a[2 + i]
    for y in range(10):
      if dp[i][y] == 0:
        continue
      print("x: " + str(x) + " y:" + str(y))
      dp[i + 1][(x + y) % 10] = (dp[i + 1][(x + y) % 10] + dp[i][y]) % MOD
      dp[i + 1][(x * y) % 10] = (dp[i + 1][(x * y) % 10] + dp[i][y]) % MOD

  for v in dp[n - 1]:
    print(v)


if __name__ == '__main__':
  main()
