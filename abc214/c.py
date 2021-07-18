def main():
  n = int(input())
  s = list(map(int, input().split()))
  t = list(map(int, input().split()))

  now_time = 10**9 + 1
  time_list = []
  for i in range(n):
    if now_time > t[i]:
      now_time = t[i]

    time_list.append(now_time)

    now_time += s[i]

  now_time = time_list[n - 1] + s[n - 1]

  for i in range(n):
    if now_time > t[i]:
      now_time = t[i]

    time_list[i] = now_time

    now_time += s[i]

  for i in range(n):
    print(time_list[i])

if __name__ == '__main__':
  main()