a = input()
b = input()
a = int(a)
b = int(b)
if a==0 and b>=19:
    print("MAN")
elif a==0 and b<19:
    print("BOY")
elif a==1 and b>=19:
    print("WOMAN")
else:
    print("GIRL")