def main():
    n = int(input())
    flg = [True] * (2 * n + 2)
    flg[0] = False

    def search():
        for i in range(2 * n + 2):
            if flg[i]:
                return i

        return -1

    while True:
        call = search()
        flg[call] = False
        print(call)

        res = int(input())
        if res == 0:
            exit()
        flg[res] = False


if __name__ == "__main__":
    main()
