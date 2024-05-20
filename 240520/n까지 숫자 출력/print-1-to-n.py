n = int(input())
flag = True
i = 1

while flag:
    if i>n:
        flag = False
        continue
    print(i,end = " ")
    i += 1