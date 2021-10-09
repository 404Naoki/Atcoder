def main():
  from collections import deque

  n = int(input())
  a = list(map(int, input().split()))

  dq = deque()
  for i in range (n):
    dq.append((a[i], i % 2))

  now = 1
  ans = 0
  while len(dq) > 1:
    l = dq.popleft()
    r = dq.pop()

    if l[1] == r[1]:
      if l[0] < r[0]:
        dq.append(r)
        ans += l[0]
        dq.appendleft((dq.popleft()[0] + l[0] + 1, now))
      else :
        dq.appendleft(l)
        ans += r[0]
        dq.append((dq.pop()[0] + r[0] + 1, now))

    elif now != l[1]:
      dq.append(r)
      ans += l[0]
      dq.appendleft((dq.popleft()[0] + l[0] + 1, now))

    else :
      dq.appendleft(l)
      ans += r[0]
      dq.append((dq.pop()[0] + r[0] + 1, now))

    now = (now + 1) % 2

  print(ans)

if __name__ == '__main__':
  main()
