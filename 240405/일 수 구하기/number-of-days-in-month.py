n = input()
n = int(n)
# 1 3 5 7 8 10 12 31일
# 4 6 9 11 30일
# 2 28일
if n==2:
    print("28")
elif n<=7:
    if n%2==1:
        print("31")
    else:
        print("30")
else:
    if n%2==0:
        print("31")
    else:
        print("30")