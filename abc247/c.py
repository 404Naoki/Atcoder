def func(n, side):
    ret = []
    if n > 0:
        if side > 0:
            for x in func(n - 1, side - 1):
                ret.append(str(x))
        ret.append(str(n))
        if side > 0:
            for x in func(n - 1, side - 1):
                ret.append(str(x))
    return ret


def main():
    n = int(input())
    ans = func(n, n - 1)
    print(" ".join(ans))


if __name__ == "__main__":
    main()
