def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))

    c_max = -1
    a_min = 2 * (10 ** 5) + 1
    for i in range(n):
        v = w[i]
        if s[i] == "0":
            c_max = max(c_max, v)
        else:
            a_min = min(a_min, v)
    c_max += 0.1

    c_ans = 0
    a_ans = 0
    for i in range(n):
        if s[i] == "0":
            if w[i] < c_max:
                c_ans += 1
            if w[i] < a_min:
                a_ans += 1

        if s[i] == "1":
            if w[i] >= c_max:
                c_ans += 1
            if w[i] >= a_min:
                a_ans += 1

    print(max(c_ans, a_ans))


if __name__ == "__main__":
    main()
