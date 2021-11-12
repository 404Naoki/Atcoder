def main():
  import math

  n, m = map(int, input().split())

  b = []
  for _ in range(n):
    row = list(map(int, input().split()))
    b.append(row)

  for j in range(1, 7 - m + 2):
    i_dec = (b[0][0] - j) / 7

    if int(i_dec) != int(math.ceil(i_dec)):
      continue
    i_dec = int(i_dec)

    flg = True
    for y in range(n):
      for x in range(m):
        ans = (i_dec + y) * 7 + (j + x)
        if ans != b[y][x]:
          flg = False
          break
      if not flg:
        break
    if flg:
      print("Yes")
      exit()

  print("No")

if __name__ == '__main__':
  main()
