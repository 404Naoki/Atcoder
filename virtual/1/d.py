def main():
  n = int(input())
  ng = []

  for _ in range(3):
    ng.append(int(input()))

  dp = [101] * (n + 1)

  dp[0] = 0
  for i in range(n + 1):
    if dp[i] >= 100:
      continue

    for j in range(1, 4):
      to = i + j
      if to > n:
        break

      flg = True
      for x in ng:
        if to == x:
          flg = False
          break

      if flg:
        dp[to] = min(dp[to], dp[i] + 1)

  if dp[n] <= 100:
    print("YES")
  else :
    print("NO")


if __name__ == '__main__':
  main()