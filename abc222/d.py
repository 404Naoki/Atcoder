from typing import AnyStr


def main():
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  MOD = 998244353
  ans = b[0] - a[0] + 1
  for i in range(1, n):
    b_back = b[i - 1]
    t_sum = 0
    for j in range(a[i], b_back + 1):
      t_sum += j - a[i]
    ans = (ans * (b[i] - a[i] + 1) - t_sum) % MOD

  print(ans)

if __name__ == '__main__':
  main()
