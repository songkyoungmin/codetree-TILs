b,a = map(int,input().split(" "))
flag = True
i = b
if i%2==0:
    while flag:
        if i <a:
            flag = False
            continue
        print(i,end = " ")
        i -= 2