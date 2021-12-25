n, x = map(int, input().split())
a = []
for _ in range(n):
    line = list(map(int, input().split()))
    a.append(line[1:])

ans = 0


def dfs(pos, seki):
    global ans, x
    if pos == n:
        if seki == x:
            ans += 1
    else:
        for v in a[pos]:
            dfs(pos + 1, seki * v)


dfs(0, 1)
print(ans)
