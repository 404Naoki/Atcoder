def find_head(tree, key):
    ret = key
    while tree[ret][0] != 0:
      ret = tree[ret][0]

    return ret

def main():
  n, q = map(int, input().split())

  prev = [0] * (n + 1)
  next = [0] * (n + 1)

  for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
      x = query[1]
      y = query[2]

      next[x] = y
      prev[y] = x

    if query[0] == 2:
      x = query[1]
      y = query[2]

      next[x] = 0
      prev[y] = 0

    if query[0] == 3:
      x = query[1]

      p = x
      while prev[p] != 0:
        p = prev[p]

      out = [str(p)]
      while next[p] != 0:
        p = next[p]
        out.append(str(p))

      out = [str(len(out))] + out
      print(" ".join(out))

if __name__ == '__main__':
  main()
