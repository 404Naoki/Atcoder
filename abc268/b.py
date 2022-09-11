def main():
    s = input()
    t = input()

    if len(s) > len(t):
        print("No")
        exit()

    t_cut = t[0: len(s)]

    if t_cut == s:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
