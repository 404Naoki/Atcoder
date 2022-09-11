from bisect import bisect_left
import heapq


def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    ans = [-1] * (n + 1)
    ba = []

    for d in p:
        idx = bisect_left(ba, key=lambda x: x[0])
        if idx >= len(ba):
            ba.append([d, 1])
        else:
            ba[idx] = [d, ba[idx][1] + 1]
            if ba[idx][1] >= k:
                ba.pop[idx]
                



if __name__ == "__main__":
    main()
