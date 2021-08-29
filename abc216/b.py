def main():
  n = int(input())
  names = []

  for i in range(n):
    names.append(input())

  names.sort()

  flg = True
  for i in range(n - 1):
    if names[i] == names[i + 1]:
      print("Yes")
      flg = False
      break

  if flg:
    print("No")

if __name__ == '__main__':
  main()