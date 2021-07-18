def main():
  a, b = map(int, input().split())
  ab = a + b
  if(ab - a > 0 and ab - b > 0):
    print("Alloy")
  elif(ab - b > 0):
    print("Gold")
  else :
    print("Silver")

if __name__ == '__main__':
  main()