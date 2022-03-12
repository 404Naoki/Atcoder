def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    flg = [False] * (n + 1)

    p = x
    while not flg[p]:
        flg[p] = True
        p = a[p - 1]

    print(flg.count(True))


if __name__ == "__main__":
    main()
