def main():
  from heapq import heappop, heapify

  q = int(input())

  a = []
  for _ in range(q):
    query = list(map(int, input().split()))
    n = query[0]
    if n == 1:
      x = query[1]
      a.append(x)
    if n == 2:
      print(a[0])
    if n == 3:
      heapify(a)

if __name__ == '__main__':
  main()