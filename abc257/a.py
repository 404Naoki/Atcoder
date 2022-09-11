def main():
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n, x = map(int, input().split())

    p = int((x - 1) / n)
    print(a[p])


if __name__ == "__main__":
    main()
