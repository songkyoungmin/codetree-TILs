# # res1,tem1 = input().split(" ")
# # res2,tem2 = input().split(" ")
# # res3,tem3 = input().split(" ")
# # res1 = str(res1)
# # res2 = str(res2)
# # res3 = str(res3)
# # tem1 = int(tem1)
# # tem2 = int(tem2)
# # tem3 = int(tem3)
# # if res1=='Y' and tem1>=37:
# #     print("A")
# # elif res1 == 'N' and tem1>=37:
# #     print("B")
# # elif res1 == 'Y'and tem1<=37:
# #     print("C")
# # else:
# #     print("D")
# # if res2=='Y' and tem2>=37:
# #     print("A")
# # elif res2 == 'N' and tem2>=37:
# #     print("B")
# # elif res2 == 'Y'and tem2<=37:
# #     print("C")
# # else:
# #     print("D")
# # if res3=='Y' and tem3>=37:
# #     print("A")
# # elif res3 == 'N' and tem3>=37:
# #     print("B")
# # elif res3 == 'Y'and tem3<=37:
# #     print("C")
# # else:
# #     print("D")
# # if 'A'>=2:
# #     print("E")
# # else:
# #     print("N")\

# res1,tem1 = input().split(" ")
# res2,tem2 = input().split(" ")
# res3,tem3 = input().split(" ")
# res1 = str(res1)
# res2 = str(res2)
# res3 = str(res3)
# tem1 = int(tem1)
# tem2 = int(tem2)
# tem3 = int(tem3)
# 'A'= res1=='Y'and tem1>=37
# 'B'= res2=='N'and tem2>=37
# 'C'= res3 =='Y'and tem3<37
# 'D'= 

res1,tem1 = input().split(" ")
res2,tem2 = input().split(" ")
res3,tem3 = input().split(" ")
res1 = str(res1)
res2 = str(res2)
res3 = str(res3)
tem1 = int(tem1)
tem2 = int(tem2)
tem3 = int(tem3)
if res1 == 'Y' and tem1>=37:
     if res3 == 'Y' and tem3>=37:
        print('E')
        if res2 == 'Y' and tem2>=37:
            print('E')
        else:
            ('N')