a,b = input().split(" ")
a = int(a)
b = int(b)
if a>=90 and 95<=b:
    print(100000)
elif a>=90 and 95>b>=90:
    print(50000)
else:
    print(0)