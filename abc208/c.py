def main():
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  
  b = [x for x in a]
  b.sort()

  all = k // n
  k %= n

  for x in a:
    if k > 0 and x <= b[k - 1]:
      print(all + 1)
    else:
      print(all)


if __name__ == '__main__':
  main()
