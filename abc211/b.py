ans = ["H", "2B", "3B", "HR"]
ans.sort()

s = []
for i in range(4):
  s.append(input())

s.sort()

if ans == s:
  print("Yes")
else :
  print("No")