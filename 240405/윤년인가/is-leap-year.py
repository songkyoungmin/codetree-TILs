y = input()
y = int(y)
if y%4==0:
    if y%100==0 or y%400!=0:
        print("true")
else:
    print("false")