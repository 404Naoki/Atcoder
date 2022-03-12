def main():
    n = int(input())
    if n < 10:
        print("AGC00{}".format(n))
    elif n < 42:
        print("AGC0{}".format(n))
    else:
        print("AGC0{}".format(n + 1))


if __name__ == "__main__":
    main()
