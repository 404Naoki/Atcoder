def main():
    n, m = map(int, input().split())

    edge = [[False for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        edge[u][v] = True
        edge[v][u] = True

    ans = 0
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                e_a = edge[a][b]
                e_b = edge[b][c]
                e_c = edge[c][a]
                if e_a and e_b and e_c:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
