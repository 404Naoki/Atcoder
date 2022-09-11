def main():
    n, x, y = map(int, input().split())

    dp = [[0, 0] for _ in range(n + 1)]
    dp[n][0] = 1

    for i in reversed(range(2, n + 1)):
        r = dp[i][0]
        dp[i - 1][0] += r
        dp[i][1] += r
        b = dp[i][1]
        dp[i - 1][0] += b
        dp[i - 1][1] += b * y

    print(dp[1][1])


if __name__ == "__main__":
    main()
