def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans_1 = 0
    ans_2 = 0
    for i in range(n):
        A = a[i]
        for j in range(n):
            B = b[j]
            if A == B:
                if i == j:
                    ans_1 += 1
                else:
                    ans_2 += 1

    print(ans_1)
    print(ans_2)


if __name__ == "__main__":
    main()
