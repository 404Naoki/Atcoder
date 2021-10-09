from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

def main():
    n, m = map(int, input().split())
    uf = UnionFind(n)

    edges = []
    sum_c = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        sum_c += max(0, c)
        if c < 0 or a == b:
            c = 0
        edges.append((c, a - 1, b - 1))
    edges.sort()

    cost = 0
    for edge in edges:
        w, s, t = edge
        if not uf.same(s, t):
            cost += w
            uf.union(s, t)
    print(sum_c - cost)

if __name__ == '__main__':
    main()
