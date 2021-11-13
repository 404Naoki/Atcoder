def main():
    n = int(input())
    s = list(map(int, input().split()))

    s_max = max(s)
    ans_list = []
    for a in range(1, s_max + 1):
        for b in range(1, s_max + 1):
            res = (4 * a * b) + (3 * a) + (3 * b)
            if res > s_max:
                break
            ans_list.append(res)

    cnt = 0
    for x in s:
        if not (x in ans_list):
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
