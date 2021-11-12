def rotate_str(str):
  return str[1:] + str[: 1]

def main():
  s = input()

  s_list = []
  s_list.append(s)
  tmp = s
  for i in range(len(s)):
    tmp = rotate_str(tmp)
    s_list.append(tmp)

  s_list.sort()
  print(s_list[0])
  print(s_list[len(s_list) - 1])


if __name__ == '__main__':
  main()
