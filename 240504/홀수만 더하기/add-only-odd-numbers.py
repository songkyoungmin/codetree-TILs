sum = 0
n = int(input())
for i in range(n):
    if i % 3 ==0 and i%2==1:
        sum+=i
print(sum)