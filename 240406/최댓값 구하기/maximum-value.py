a,b,c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
if a>=b>=c and a>=c>=b:
    print(a)
elif b>=a>=c and b>=c>=a:
    print(b)
elif c>=a>=b and c>=b>=a:
    print(c)
else:
    print(" ")