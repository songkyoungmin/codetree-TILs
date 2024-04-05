a,b,c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
if a>=b>=c:
    if c>=b>=a:
        print(b)
    elif a>=c>=b:
        if b>=c>=a:
            print(c)
else:
    print(a)