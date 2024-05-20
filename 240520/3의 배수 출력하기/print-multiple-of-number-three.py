n = int(input())
flag = True
i = 3

while flag:
    if i>n:
        flag = False
        continue
    print(i,end = " ")
    i += 3