def main():
    s = input()
    ans = ["0"]
    for i in range(3):
        if s[i] == "1":
            ans.append("1")
        else:
            ans.append("0")

    print("".join(ans))


if __name__ == "__main__":
    main()
