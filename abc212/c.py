def main():
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  a.sort()
  b.sort()

  ans = 10**9 + 1
  i_a = 0;
  i_b = 0;
  while(i_a < n and i_b < m):
    ans = min(ans, abs(a[i_a] - b[i_b]))
    if(a[i_a] <= b[i_b]):
      i_a += 1
    elif(a[i_a] > b[i_b]):
      i_b += 1

  print(ans)

if __name__ == '__main__':
  main()