def main():
    mod = 998244353

    n, m, k, s, t, x = map(int, input().split())
    edge = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)

    dp = [[[0, 0] for _ in range(n + 1)] for _ in range(k + 1)]
    dp[0][s][0] = 1

    for a in range(k):
        for b in range(n + 1):
            for c in range(2):
                if dp[a][b][c] == 0:
                    continue
                val = dp[a][b][c]
                for e in edge[b]:
                    to_c = c
                    if e == x:
                        to_c += 1
                        to_c %= 2
                    to_val = dp[a + 1][e][to_c]
                    dp[a + 1][e][to_c] = (to_val + val) % mod

    print(dp[k][t][0])


if __name__ == "__main__":
    main()
