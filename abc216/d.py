def main():
  from heapq import heappop, heappush

  n, m = map(int, input().split())
  k = []
  a = []

  for i in range(m):
    k.append(int(input()))
    a.append(list(map(int, input().split())))

  flg = True
  while len(a) >= 2:
    a.sort()
    p = -1
    for i in range(len(a) - 1):
      if a[i][0] == a[i + 1][0]:
        p = i
        break

    if p < 0 or len(a) == 1:
      print('No')
      flg = False
      break

    x = a.pop(i)
    y = a.pop(i)

    x.pop(0)
    y.pop(0)

    if len(x) > 0:
      a.append(x)
    if len(y) > 0:
      a.append(y)

  if flg:
    print('Yes')


if __name__ == '__main__':
  main()