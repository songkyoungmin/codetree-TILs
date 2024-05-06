sum = 0 
cnt = 0
for i in range(10):
    a = int(input())
    if a>=0 and 200>=a:
        sum += a
        cnt += 1
        avg = sum / cnt
print(f"{sum} {avg:.1f}")