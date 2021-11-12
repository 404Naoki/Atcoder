def main():
  n, p = map(int, input().split())
  a = list(map(int, input().split()))

  a_d = [x < p for x in a]

  print(sum(a_d))

if __name__ == '__main__':
  main()