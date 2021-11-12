def janken(a, b):
  if a == b:
    return [0, 0]
  elif a == 'G' and b == 'C':
    return [-1, 0]
  elif a == 'C' and b == 'P':
    return [-1, 0]
  elif a == 'P' and b == 'G':
    return [-1, 0]
  else :
    return [0, -1]

def main():
  n, m = map(int, input().split())
  a = []
  for _ in range(n * 2):
    a.append(input())

  point = []
  for i in range(n * 2):
    point.append([0, i])

  for i in range(m):
    for k in range(n):
      p1 = 2 * k
      p2 = p1 + 1
      result = janken(a[point[p1][1]][i], a[point[p2][1]][i])
      point[p1][0] += result[0]
      point[p2][0] += result[1]
    point.sort()

  point.sort(key= lambda x: x[1])
  point.sort()

  for x in point:
    print(x[1] + 1)

if __name__ == '__main__':
  main()
