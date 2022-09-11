def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))

    for x in l:
        x -= 1
        if a[x] == n:
            continue

        m = a[x] + 1
        if not (m in a):
            a[x] += 1

    print(" ".join(map(str, a)))


if __name__ == "__main__":
    main()
