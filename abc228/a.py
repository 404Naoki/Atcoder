def main():
    s, t, x = map(int, input().split())
    matagi_flg = s > t
    if matagi_flg:
        if x >= s or x < t:
            print("Yes")
            exit()
    else:
        if x >= s and x < t:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
