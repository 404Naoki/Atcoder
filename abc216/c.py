def main():
  n = int(input())

  ans = []
  while n > 1:
    if n % 2 == 1:
      ans.append('A')

    n //= 2
    ans.append('B')

  ans.append('A')
  ans.reverse()
  print(''.join(ans))

if __name__ == '__main__':
  main()