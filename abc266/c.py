def inside_polygon(p0, qs):
    cnt = 0
    L = len(qs)
    x, y = p0
    for i in range(L):
        x0, y0 = qs[i - 1]
        x1, y1 = qs[i]
        x0 -= x
        y0 -= y
        x1 -= x
        y1 -= y

        cv = x0 * x1 + y0 * y1
        sv = x0 * y1 - x1 * y0
        if sv == 0 and cv <= 0:
            return True

        if not y0 < y1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        if y0 <= 0 < y1 and x0 * (y1 - y0) > y0 * (x1 - x0):
            cnt += 1

    return cnt % 2 == 1


def main():
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    dx, dy = map(int, input().split())

    flg = True

    p = [ax, ay]
    tr = [[bx, by], [cx, cy], [dx, dy]]
    if inside_polygon(p, tr):
        flg = False

    p = [bx, by]
    tr = [[cx, cy], [dx, dy], [ax, ay]]
    if inside_polygon(p, tr):
        flg = False

    p = [cx, cy]
    tr = [[dx, dy], [ax, ay], [bx, by]]
    if inside_polygon(p, tr):
        flg = False

    p = [dx, dy]
    tr = [[ax, ay], [bx, by], [cx, cy]]
    if inside_polygon(p, tr):
        flg = False

    if flg:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
