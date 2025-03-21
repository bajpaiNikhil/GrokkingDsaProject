bills = [5,5,10,10,20]



fiveBillCount = 0
tenBillCount = 0
twentyBillCount = 0

for i in bills:
    if i == 5:
        fiveBillCount += 1
    elif i == 10:
        if fiveBillCount == 0:
            print("1",False)
            exit(False)
        fiveBillCount -= 1
        tenBillCount += 1
    else:
        if tenBillCount > 0 and fiveBillCount > 0:
            tenBillCount -= 1
            fiveBillCount -= 1
        elif fiveBillCount >= 3:
            fiveBillCount -= 3
        else:
            print("2",False)
            exit(False)
print(True)
exit(True)
# fiveCount = 0
# tenCount = 0
# twentyCount = 0
# for i in bills:
#     if i == 5:
#         fiveCount += 1
#     elif i == 10:
#         if fiveCount == 0:
#             print(False)
#             exit()
#         fiveCount -= 1
#         tenCount += 1
#     else: # bill 20
#         if tenCount>0 and fiveCount >0:
#             tenCount-=1
#             fiveCount-=1
#         elif fiveCount>=3:
#             fiveCount-=3
#         else:
#             print(False)
#             exit()
#
# print(True)
# exit()
