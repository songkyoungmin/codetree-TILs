# y = input()
# y = int(y)
# if y%4==0 or y%400!=0:
#     print("true")
# elif y%100!=0:
#         print("true")
# else:
#     print("false")

# 결론은 4로 나누어지거나 400으로도 나누어 떨어져야함

# y = input()
# y = int(y)
# if y%400==0:
#     print("true")
# elif y%100==0:
#     print("false")
# elif y%4==0:
#     print("true")
# else:
#     print("flase")

# y = input()
# y = int(y)
# if y%100!=0 or (y%400==0 and y%4==0):
#     print("true")
# else:
#     print("false")

y = input()
y = int(y)
# if y%400==0:
#     print("true")
# elif y%100==0:
#     print("false")
# elif y%4==0:
#     print("true")
# else:
#     print("false")
if y%4==0:
    if y%100==0:
        if y%400!=0:
            print("false")
        else:
            print("true")
    else:
        print("true")
else:
    print("false")