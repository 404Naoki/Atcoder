def main():
    n = int(input())
    a = list(map(int, input().split()))

    a = [-1] + a

    ans = 0
    cnt = 0
    for i in range(1, n + 1):
        v = a[i]
        if v == i:
            ans += cnt
            cnt += 1

        else:
            if a[v] == i and v > a[v]:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
