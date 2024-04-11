a,b = input().split(" ")
a = int(a)
b = int(b)


if a>b:
    res = a*b
    print(res)
else: #if a<=b:
    res = b//a
    print(res)