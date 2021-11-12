def main():
  n = int(input())

  cnt = [0] * n
  for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    cnt[a] += 1
    cnt[b] += 1

  for x in cnt:
    if x == (n - 1):
      print("Yes")
      exit()

  print("No")

if __name__ == '__main__':
  main()