def calc_x(a, b):
    return (a + b) * (a * a + b * b)


def main():
    a, b = map(int, input().split())
    print(calc_x(a, b))
    # n = int(input())


if __name__ == "__main__":
    main()
