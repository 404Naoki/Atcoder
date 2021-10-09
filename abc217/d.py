def main():
  import bisect
  from array import array
  l, q = map(int, input().split())

  arr = array("i", [0, l])
  for _ in range(q):
    c, x = map(int, input().split())
    if c == 1:
      bisect.insort(arr, x)
    else :
      idx = bisect.bisect(arr, x)
      print(arr[idx] - arr[idx - 1])

if __name__ == '__main__':
  main()