def main():
    n, k, a = map(int, input().split())
    ans = (k + a - 1) % n
    if ans == 0:
        ans = n
    print(ans)


if __name__ == "__main__":
    main()
