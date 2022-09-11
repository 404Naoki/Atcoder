def main():
    n, m, x, t, d = map(int, input().split())

    if x <= m <= n:
        print(t)
    else:
        z = t - (x * d)
        print(z + m * d)


if __name__ == "__main__":
    main()
