def main():
  a, b = map(int, input().split())
  if a * 6 < b or a * 1 > b:
    print("No")
  else :
    print("Yes")

if __name__ == '__main__':
  main()