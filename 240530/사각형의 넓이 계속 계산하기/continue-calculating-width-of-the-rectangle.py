while True:
    a,b,c = map(str,input().split(" "))
    a = int(a)
    b = int(b)
    sql = a*b
    print(sql)
    if c=='C':
        break