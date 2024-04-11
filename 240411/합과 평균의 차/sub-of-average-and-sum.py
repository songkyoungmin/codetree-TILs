a,b,c = map(int,input().split(" "))

sum = a+b+c
avg = sum // 3
res = sum - avg
print(sum,avg,res,sep = "\n")