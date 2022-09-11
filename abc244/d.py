def main():
    s = list(map(str, input().split()))
    t = list(map(str, input().split()))

    cnt = 0
    for i in range(3):
        if s[i] != t[i]:
            cnt += 1

    if cnt == 2:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
