def main():
  from itertools import permutations
  from collections import defaultdict

  s, k = input().split()
  k = int(k)

  d = defaultdict(int)
  for x in permutations(s):
    d[x] = 1

  print(d)

  v = [k for k in d.keys()]
  v.sort()

  print(''.join(v[k - 1]))

if __name__ == '__main__':
  main()