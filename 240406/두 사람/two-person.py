# age1,gender1 = input().split(" ")
# age1 = int(age1)
# age2,gender2 = input().split(" ")
# age2 = int(age2)
# if gender1 == M or gender2 == M:
#     if age1 >=19 or age2 >=19:
#         print(1)
# else:
#     print(0)

a,b = input().split(" ")
c,d = input().split(" ")
a = int(a)
b = str(b)
c = int(c)
d = str(d)
if a>=19 or c>=19:
    if b== 'M'or d =='M':
        print(1)
    if b=='W' and d =='W':
        print(0)
else:
    print(0)