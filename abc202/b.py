def main():
  s = input()
  sRev = s[::-1]
  
  ans = []
  for c in sRev:
    if c == "6":
      ans.append("9")
    elif c == "9":
      ans.append("6")
    else :
      ans.append(c)

  print("".join(ans))

if __name__ == '__main__':
  main()