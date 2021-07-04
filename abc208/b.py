def main():
  p = int(input())

  x = 1
  y = 2
  li = []
  li.append(x);
  while x <= p:
    x *= y
    li.append(x)
    y += 1

  li.reverse()
  cnt = 0
  for x in li:
    while x <= p:
      p -= x
      cnt += 1

  print(cnt)

if __name__ == '__main__':
  main()