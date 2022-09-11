def main():
    n = int(input())
    s = []

    for _ in range(n):
        s.append(input())

    d = {}
    for x in s:
        if x in d:
            print("{}({})".format(x, d[x]))
            d[x] = d[x] + 1

        else:
            print(x)
            d[x] = 1


if __name__ == "__main__":
    main()
