def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    for i in range(n):
        if k <= 0:
            break
        v = a[i]
        use_k = int(v / x)
        if k >= use_k:
            k -= use_k
            a[i] -= x * use_k
        else:
            a[i] -= x * k
            k = 0

    a.sort(reverse=True)
    for i in range(min(k, n)):
        a[i] = 0

    print(sum(a))


if __name__ == "__main__":
    main()
