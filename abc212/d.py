def main():
  import heapq
  q = int(input())

  bag = []
  total = 0

  for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
      heapq.heappush(bag, query[1] - total)
    elif query[0] == 2:
      total += query[1]
    elif query[0] == 3:
      print(heapq.heappop(bag) + total)

if __name__ == '__main__':
  main()