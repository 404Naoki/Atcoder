def main():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    n = int(input())
    t = input()

    x = 0
    y = 0
    direction = 1
    for q in t:
        if q == "R":
            direction = (direction + 1) % 4
        else:
            x += dx[direction]
            y += dy[direction]

    print(x, y)


if __name__ == "__main__":
    main()
