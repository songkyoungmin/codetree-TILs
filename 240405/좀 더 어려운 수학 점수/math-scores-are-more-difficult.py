m1,e1 = input().split(" ")
m2,e2 = input().split(" ")
m1 = int(m1)
e1 = int(e1)
m2 = int(m2)
e2 = int(e2)
if m1>m2 or (e1<e2 and e2==e1):
    print("A")
else:
    print("B")