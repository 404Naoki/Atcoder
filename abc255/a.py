def main():
    r, c = map(int, input().split())
    a = []
    a.append(list(map(int, input().split())))
    a.append(list(map(int, input().split())))

    print(a[r - 1][c - 1])


if __name__ == "__main__":
    main()
