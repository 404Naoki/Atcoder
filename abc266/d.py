def main():
    n = int(input())
    ts = [[0 for i in range(6)] for j in range(10 ** 5 + 1)]

    for _ in range(n):
        t, x, a = map(int, input().split())
        ts[t][x] = a

    dp = [[-1 for i in range(6)] for j in range(10 ** 5 + 2)]
    dp[0][0] = 0
    for i in range(10 ** 5 + 1):
        for j in range(6):
            if dp[i][j] < 0:
                continue

            dp[i][j] += ts[i][j]
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j > 0:
                dp[i + 1][j - 1] = max(dp[i + 1][j - 1], dp[i][j])
            if j < 5:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])

    print(max(dp[10 ** 5 + 1]))


if __name__ == "__main__":
    main()
