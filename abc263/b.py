def main():
    n = int(input())
    p = list(map(int, input().split()))

    cnt = 1
    i = p[n - 2]
    while i != 1:
        i = p[i - 2]
        cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
