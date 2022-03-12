def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    k1_min = max(1 - a, 1 - b)
    k1_max = min(n - a, n - b)
    k2_min = max(1 - a, b - n)
    k2_max = min(n - a, b - 1)
    


if __name__ == "__main__":
    main()
