a, b, c = input().split()
if (a == b and b == c) :
    print("No")
elif (a == b or a == c or b == c) :
    print("Yes")
else :
    print("No")