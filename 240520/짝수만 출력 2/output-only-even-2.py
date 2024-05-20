b,a = map(int,input().split(" "))
flag = True
i = b

while flag:
    if i <a:
        flag = False
        continue
    print(i,end = " ")
    i -= 2