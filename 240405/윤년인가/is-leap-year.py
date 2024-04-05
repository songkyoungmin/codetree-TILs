y = input()
y = int(y)
if y%4==0 or y%400!=0:
    print("true")
elif y%100!=0:
        print("true")
else:
    print("false")

# 4로 나누어지거나 400으로도 나누어 떨어져야함