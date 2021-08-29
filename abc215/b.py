def main():
  from math import log2, floor
  n = int(input())

  ans = floor(log2(n))

  if 2**ans > n:
    print(ans - 1)
  else :
    print(ans)

if __name__ == '__main__':
  main()