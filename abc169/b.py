n = int(input())
a = list(map(int, input().split()))
ans = 1
for i in range(n):
    if a[i] == 0:
        ans = 0
    if ans != -1:
        ans = ans * a[i]
    if ans > 1000000000000000000:
        ans = -1
print(ans)