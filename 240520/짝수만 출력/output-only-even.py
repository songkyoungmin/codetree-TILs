a,b = map(int,input().split(" "))
flag = True
i = a

while flag:
    if i>b:
        flag = False
        continue
    print(i,end = " ")
    i += 2