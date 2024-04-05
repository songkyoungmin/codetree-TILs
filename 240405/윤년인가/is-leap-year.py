y = input()
y = int(y)
if y%4==0:
    print("true")
elif y%100==0 and y%400==1:
    print("false")
else:
    print("false")