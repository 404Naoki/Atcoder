import heapq

def dijkstra(s):
  hq = [(0, s)]
  heapq.heapify(hq) # リストを優先度付きキューに変換
  cost = [float('inf')] * n # 行ったことのないところはinf
  cost[s] = 0 # 開始地点は0
  while hq:
    c, v = heapq.heappop(hq)
    if c > cost[v]: # コストが現在のコストよりも高ければスルー
      continue
    for d, u in e[v]:
      tmp = d + cost[v]
      if tmp < cost[u]:
        cost[u] = tmp
        heapq.heappush(hq, (tmp, u))
  return cost

n,m = map(int,input().split())

e = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    t = a
    a,b = a-1, b-1
    e[a].append((t, b))

cnt = 0
for i in range(n):
    dist = dijkstra(i)
    for val in dist:
      if (val != float('inf')):
        cnt = cnt + 1

print(cnt)