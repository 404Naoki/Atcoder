from collections import defaultdict


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a_sums = [0]
    for i, x in enumerate(a):
        a_sums.append(a_sums[i] + x)

    ans = 0
    d = defaultdict(int)
    d[0] = 1
    for x in a_sums[1:]:
        ans += d[x - k]
        d[x] += 1

    print(ans)


if __name__ == "__main__":
    main()
