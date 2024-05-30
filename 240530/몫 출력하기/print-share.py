a = 0

while True:
    n = int(input())
    if n%2==1:
        continue

    print(n//2)
    a += 1

    if a>=3:
        break