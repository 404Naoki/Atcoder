def main():
  alf = "abcdefghijklmnopqrstuvwxyz"
  p = list(map(int, input().split()))

  ans = []
  for x in p:
    ans.append(alf[x - 1])

  print("".join(ans))

if __name__ == '__main__':
  main()
