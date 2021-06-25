n = int(input())

t = list(map(int, input().split()))

ans = 1000000000
def func(i, x, y):
  if i == n:
    global ans
    ans = min(ans, max(x, y))
    return 0
  else :
    func(i + 1, x + t[i], y)
    func(i + 1, x, y + t[i])

func(0, 0, 0)

print(ans)
