# age1,gender1 = input().split(" ")
# age1 = int(age1)
# age2,gender2 = input().split(" ")
# age2 = int(age2)
# if gender1 == M or gender2 == M:
#     if age1 >=19 or age2 >=19:
#         print(1)
# else:
#     print(0)

age1,gen1 = input().split(" ")
age2,gen2 = input().split(" ")
age1 = int(age1)
age2 = int(age2)

# if age1>=19 and age2>=19:
#     if gen1== 'M'and gen2 =='M':
#         print(1)
#     else:
#         print(0)
# else:
#     print(0)

if (age1 >=19 and gen1 == 'M') or (age2 >=19 and gen2 == 'M'):
    print(1)
else:
    print(0)