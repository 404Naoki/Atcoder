def main():
    y = int(input())

    while 1:
        if y % 4 == 2:
            print(y)
            exit()
        y += 1


if __name__ == "__main__":
    main()
