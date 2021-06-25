a, b, x = map(int, input().split())

def price(n):
    return a * n + b * len(str(n))

high = 10 ** 9 + 1
low = 0

while high - low > 1:
    mid = (high + low) // 2
    v = price(mid)
    if v > x:
        high = mid
    else:
        low = mid
print(low)