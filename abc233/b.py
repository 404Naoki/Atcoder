def main():
    l, r = map(int, input().split())
    s = input()

    s_1 = s[: l - 1]
    s_2 = s[l - 1 : r]
    s_3 = s[r:]

    s_2 = s_2[::-1]

    print("".join([s_1, s_2, s_3]))


if __name__ == "__main__":
    main()
