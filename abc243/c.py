def main():
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        X, Y = map(int, input().split())
        x.append(X)
        y.append(Y)
    s = input()

    humans = []
    for i in range(n):
        X = x[i]
        Y = y[i]
        if s[i] == "R":
            S = 0
        else:
            S = 1
        humans.append({"x": X, "y": Y, "s": S})
    humans = sorted(humans, key=lambda x: x["x"])

    ys = dict()
    for human in humans:
        X = human["x"]
        Y = human["y"]
        S = human["s"]
        if S == 0 and Y not in ys:
            ys[Y] = True
        if S == 1 and Y in ys:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
