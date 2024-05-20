n = int(input())
flag = True
i = n 

while flag:
    if i<1:
        flag = False
        continue
    print(i,end=" ")
    i -= 1