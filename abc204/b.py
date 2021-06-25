n = int(input())

ans = 0

arr = map(int, input().split())

for a in arr:
  ans = ans + ((a - 10) if a > 10 else 0)

print(ans)