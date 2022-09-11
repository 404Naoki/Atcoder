from math import sqrt


def main():
    x, y = map(int, input().split())

    dis = sqrt(x * x + y * y)

    print(x / dis, y / dis)


if __name__ == "__main__":
    main()
