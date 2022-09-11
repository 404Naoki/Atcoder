def main():
    count = [0] * 101

    a = list(map(int, input().split()))

    ans = 0
    for x in a:
        if count[x] == 0:
            ans += 1

        count[x] = 1

    print(ans)


if __name__ == "__main__":
    main()
