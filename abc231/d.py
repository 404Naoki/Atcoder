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

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def main():
    n, m = map(int, input().split())
    cnt = [0] * (n + 1)

    q = []

    for _ in range(m):
        a, b = map(int, input().split())
        q.append([a, b])
        cnt[a] += 1
        cnt[b] += 1

    for x in cnt:
        if x > 2:
            print('No')
            exit()

    uf = UnionFind(n + 1)
    for a, b in q:
        if uf.find(a) == uf.find(b):
            print("No")
            exit()
        else :
            uf.union(a, b)

    print("Yes")

if __name__ == '__main__':
    main()