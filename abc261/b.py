def main():
    n = int(input())
    a = []

    for _ in range(n):
        a.append(input())

    for i in range(n):
        for j in range(n):
            x = a[i][j]
            y = a[j][i]

            if i != j:
                if x == "D":
                    if x != y:
                        print("incorrect")
                        exit()
                elif x == y:
                    print("incorrect")
                    exit()

    print("correct")


if __name__ == "__main__":
    main()
