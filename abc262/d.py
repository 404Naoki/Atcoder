MOD = 998244353

def main():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [[[-1, 0] for _ in range(n + 1)] for _ in range(n + 2)]

    dp[0][0] = [0, 0]
    for i in range(n):
        x = a[i]
        for j in range(n):
            v = dp[i][j]
            if v[0] == -1:
                continue

            dp[i + 1][j] = v

            c = j + 1
            z = [v[0] + x, (v[1] + dp[i + 1][c][1]) %]
            if (z[0] / c).is_integer():
                print("ok")
                z[1] = (z[1] + 1) % 998244353
            dp[i + 1][j + 1] = z

    ans = 0
    for i in range(n + 1):
        ans += dp[n][i][1]

    print(ans)


if __name__ == "__main__":
    main()
