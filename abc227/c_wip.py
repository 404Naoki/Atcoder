def main():
    n = int(input())

    cnt = n // 2
    for c in range(1, (n // 2) + 1):
        ab = n // c
        ab = min(ab, c)
        for b in range(1, ab + 1):
            a = ab // b
            cnt += min(a, b)

    print(cnt)


if __name__ == "__main__":
    main()
