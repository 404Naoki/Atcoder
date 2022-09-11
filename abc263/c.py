def main():
    n, m = map(int, input().split())

    def func(cnt, low, arr):
        if cnt >= n:
            print(" ".join(arr))

        else:
            for i in range(low + 1, m + 1):
                func(cnt + 1, i, arr + [str(i)])

    func(0, 0, [])


if __name__ == "__main__":
    main()
