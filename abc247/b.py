import collections


def main():
    n = int(input())
    kouho = []
    s = []
    t = []
    for _ in range(n):
        ss, tt = map(str, input().split())
        s.append(ss)
        t.append(tt)
        kouho.append(ss)
        kouho.append(tt)

    cnt = collections.Counter(kouho)
    for i in range(n):
        ss = s[i]
        tt = t[i]
        if ss == tt and cnt[ss] == 2:
            continue
        if cnt[ss] >= 2 and cnt[tt] >= 2:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
