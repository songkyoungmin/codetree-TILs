n = input()
n = int(n)
if (n%2==1 and n%3==0) or (n%2==0 and n%5==0): 
    print("true")
else:
    print("false")