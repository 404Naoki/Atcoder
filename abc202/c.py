def main():
  from collections import Counter

  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  c = list(map(int, input().split()))

  cnt = Counter(a)

  ans = 0
  for p in c:
    p -= 1
    key = b[p]
    ans += cnt[key]

  print(ans)

if __name__ == '__main__':
  main()