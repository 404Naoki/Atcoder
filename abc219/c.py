def main():
  x = input()
  n = int(input())
  s = []
  for _ in range(n):
    s.append(input())

  s_num = []
  for v in s:
    v_tmp = []
    for t in v:
      v_tmp.append(x.find(t))
    s_num.append(v_tmp)

  s_num.sort()
  for v in s_num:
    ans = []
    for t in v:
      ans.append(x[t])
    print("".join(ans))


if __name__ == '__main__':
  main()
