m = input()
m = int(m)
# if m==3 or m==4 or m==5: 
#     print("Spring")
# if m==6 or m==7 or m==8:
#     print("Summer")
# if m==9 or m==10 or m==11:
#     print("Fall")
# if m==12 or m==1 or m==2:
#     print("Winter")

if 6>m and m>2:
    print("Spring")
elif m>5 and 9>m:
    print("Summer")
elif m>8 and 12>m:
    print("Fall")
else:
    print("Winter")