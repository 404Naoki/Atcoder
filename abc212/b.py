def check(string):
  f = "1234567890"
  flg = True
  for i in range(3):
    if(f[int(string[i])] != string[i + 1]):
      flg = False
      break

  return flg

def main():
  x = input()
  if(len(set(x)) == 1):
    print("Weak")
  elif(check(x)):
    print("Weak")
  else :
    print("Strong")


if __name__ == '__main__':
  main()