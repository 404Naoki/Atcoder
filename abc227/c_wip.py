def main():
    from math import pow
    n = int(input())

    cnt = 0
    for a in range(1, n + 1):
        if pow(a, 3) > n:
            break

        

    print(cnt)


if __name__ == "__main__":
    main()
