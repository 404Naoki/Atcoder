import bisect

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    for i in range(n):
        a[i] += 1

    for _ in range(q):
        x = int(input())
        i = bisect.bisect_right(a, x)
        print(n - i)


if __name__ == '__main__':
    main()