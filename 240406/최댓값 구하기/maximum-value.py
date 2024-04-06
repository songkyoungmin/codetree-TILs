a,b,c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
if a>=b>=c and a>=c>=b:
    print(a)
elif b>=a>=c and b>=c>=a:
    print(b)
else:
    print(c)