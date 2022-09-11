import collections


def main():
    x_list = []
    y_list = []
    for _ in range(3):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)

    x_cnt = collections.Counter(x_list)
    y_cnt = collections.Counter(y_list)

    x_ans = 0
    y_ans = 0
    for idx in x_cnt:
        if x_cnt[idx] == 1:
            x_ans = idx
            break

    for idx in y_cnt:
        if y_cnt[idx] == 1:
            y_ans = idx
            break

    print(x_ans, y_ans)


if __name__ == "__main__":
    main()
