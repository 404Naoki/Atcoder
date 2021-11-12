def main():
  n = int(input())

  a_l = []
  b_l = []
  for _ in  range(n):
    a, b = map(int, input().split())
    a_l.append(a)
    b_l.append(b)

  t = 0
  for i in range(n):
    t += a_l[i] / b_l[i]

  t /= 2
  ans = 0
  for i in range(n):
    ans += min(a_l[i], t * b_l[i])
    t -= min(a_l[i] / b_l[i], t)
    if t <= 0:
      break

  print(ans)

if __name__ == '__main__':
  main()