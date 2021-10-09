def main():
  ans = ["ABC", "ARC", "AGC", "AHC"]
  s = []

  for _ in range(3):
    s.append(input())

  for x in ans:
    if(not(x in s)):
      print(x)
      exit()

if __name__ == '__main__':
  main()