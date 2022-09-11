from operator import itemgetter


def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    data = []
    for i in range(n):
        data.append({"idx": i, "math": a[i], "en": b[i], "sum": a[i] + b[i]})

    ans = []
    data = sorted(data, key=itemgetter("math"), reverse=True)
    for i in range(x):
        v = data.pop(0)
        ans.append(v["idx"] + 1)

    data = sorted(data, key=itemgetter("idx"))
    data = sorted(data, key=itemgetter("en"), reverse=True)
    for i in range(y):
        v = data.pop(0)
        ans.append(v["idx"] + 1)

    data = sorted(data, key=itemgetter("idx"))
    data = sorted(data, key=itemgetter("sum"), reverse=True)
    for i in range(z):
        v = data.pop(0)
        ans.append(v["idx"] + 1)

    for i in sorted(ans):
        print(i)


if __name__ == "__main__":
    main()
