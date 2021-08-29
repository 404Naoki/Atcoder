def main():
  from heapq import heappop, heappush, heapify

  n, k = map(int, input().split())
  a = list(map(int, input().split()))

  for i in range(n):
    a[i] = a[i] * -1

  sum = 0
  while k > 0 and a[0] < 0:
    x = heappop(a) * -1
    sum += x
    k -= 1
    heappush(a, (x - 1) * -1)

  print(sum)

if __name__ == '__main__':
  main()