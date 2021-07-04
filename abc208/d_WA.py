from heapq import heappush, heappop
INF = 10 ** 9


def dijkstra(s, t, k, n, adj):  # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1]  # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]:  # ノード v に隣接しているノードに対して
            if to != to > k:
                continue
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


def main():
    n, m = map(int, input().split())

    edge = [[]] * (n + 1)

    for i in range(m):
        a, b, c = map(int, input().split())
        edge[a].append((b, c))

    ans = 0
    for s in range(1, n + 1):
        for t in range(1, n + 1):
            for k in range(1, n + 1):
                result = dijkstra(s, t, k, n + 1, edge)

                for i in range(n):
                    if result[i] == INF:
                        result[i] = 0

                ans += sum(result)

    print(ans)


if __name__ == '__main__':
    main()
