def main():
  s, t = map(int, input().split())
  s += 1
  cnt = 0
  for a in range(s):
    for b in range(s - a):
      for c in range(s - a - b):
        if (a * b * c) <= t:
          cnt += 1

  print(cnt)

if __name__ == '__main__':
  main()