def main():
  import itertools

  s = input()

  li = []
  for x in itertools.permutations(s, 3):
    li.append(x)

  print(len(set(li)))

if __name__ == '__main__':
  main()
