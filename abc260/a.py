def main():
    s = input()

    for c in s:
        cnt = s.count(c)

        if cnt == 1:
            print(c)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
