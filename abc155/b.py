n = int(input())
a = [i for i in map(int, input().split())]
flg = True
for i in range(n) :
    if a[i] % 2 == 0 :
        if (a[i] % 3 != 0 or a[i] % 5 != 0) :
            flg = False
if flg :
    print("APPROVED")
else :
    print("DENIED")