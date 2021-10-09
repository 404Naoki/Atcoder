def main():
  s = []
  for _ in range(3):
    s.append(input())

  t = input()
  ans = []
  for x in t:
    ans.append(s[int(x) - 1])

  print("".join(ans))

if __name__ == '__main__':
  main()