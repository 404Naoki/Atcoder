def main():
    s = input()

    if s == "oo":
        print("No")
        exit()

    if len(s) <= 2:
        print("Yes")
        exit()

    for i in range(1, len(s) - 1):
        if s[i] == "x":
            if s[i - 1] == s[i + 1]:
                print("No")
                exit()
        if s[i] == "o":
            if s[i - 1] == "o" or s[i + 1] == "o":
                print("No")
                exit()

    print("Yes")


if __name__ == "__main__":
    main()
