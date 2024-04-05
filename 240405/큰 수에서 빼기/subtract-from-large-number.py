a,b = input().split(" ")
a = int(a)
b = int(b)
res1 = a - b
res2 = b - a

if a > b:
    print(res1)
if b > a:
    print(res2)
else:
    print(0)