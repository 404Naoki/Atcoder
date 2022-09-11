def main():
    q = int(input())
    que = []
    idx = 0
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            c = query[2]
            que.append([x, c])

        if query[0] == 2:
            c = query[1]
            sum = 0
            while c > 0:
                num, cnt = que[idx]
                sum += num * min(c, cnt)
                c -= cnt
                if c > 0:
                    idx += 1
                else:
                    que[idx] = [num, c * -1]
            print(sum)


if __name__ == "__main__":
    main()
