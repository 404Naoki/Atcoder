def main():
    s = input()
    t = input()
    sq = []
    tq = []

    k = "0"
    n = 0
    for c in s:
        if c != k:
            sq.append([c, n])
            k = c
            n = 1
        else:
            n = n + 1

    k = "0"
    n = 0
    for c in t:
        if c != k:
            tq.append([c, n])
            k = c
            n = 1
        else:
            n = n + 1

    if len(sq) == len(tq):
        for i in range(len(sq)):
            a = sq[i]
            b = tq[i]
            if a[0] != b[0] or a[1] > b[1]:
                print("No")
                exit()
            if a[0] == b[0]:
                if a[1] == 1 and a[1] != b[1]:
                    print("No")
                    exit()
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
