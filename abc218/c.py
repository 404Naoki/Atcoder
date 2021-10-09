def main():
  n = int(input())

  s_list = []
  for i in range(n):
    line = input()
    for j in range(n):
      if line[j] == '#':
        s_list.append((j, i))

  t = []
  for i in range(n):
    t.append(input())

  for _ in range(4):
    for i in range(-n + 1, n):
      for j in range(-n + 1, n):
        flg = True
        for x, y in s_list:
          x += i
          y += j
          if not(0 <= x < n and 0 <= y < n and t[y][x] == '#'):
            flg = False
            break

        if flg:
          print("Yes")
          exit()

    s_list = [(y, n - 1 - x) for x, y in s_list]

  print("No")


if __name__ == '__main__':
  main()
