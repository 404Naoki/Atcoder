def main():
    n = int(input())
    s = []

    for _ in range(n):
        s.append(input())

    mx = -1
    mx_name = s[0]
    for name in s:
        c = s.count(name)
        if mx < c:
            mx = c
            mx_name = name

    print(mx_name)



if __name__ == '__main__':
    main()