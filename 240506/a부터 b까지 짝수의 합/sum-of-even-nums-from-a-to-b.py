a,b = map(int,input().split(" "))
sum = 0 
for i in range(a,b+1):
    if i%2==0:
        sum += i
print(sum)