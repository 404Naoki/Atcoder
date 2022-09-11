def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))

    d = {}
    for _ in range(m):
        c, y = map(int, input().split())
        d[c] = y

    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                continue

            v = dp[i][j]
            dp[i + 1][0] = max(dp[i + 1][0], v)

            v += x[i]
            if (j + 1) in d:
                v += d[(j + 1)]

            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], v)

    print(max(dp[n]))


if __name__ == "__main__":
    main()
