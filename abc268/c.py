def main():
    n = int(input())
    p = list(map(int, input().split()))

    cnt = [0] * (n + 1)
    for i in range(n):
        x = p[i]
        a = (x - 1) % n
        b = x % n
        c = (x + 1) % n

        a = n - ((a - i) % n)
        b = n - ((b - i) % n)
        c = n - ((c - i) % n)

        cnt[a] += 1
        cnt[b] += 1
        cnt[c] += 1

    print(max(cnt))


if __name__ == "__main__":
    main()
