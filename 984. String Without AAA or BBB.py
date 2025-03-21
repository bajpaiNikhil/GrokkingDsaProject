a, b = 1, 2
res = ""
while a +b >0:
    if res[-2:] == "aa":
        res+='b'
        b-=1
    elif res[-2:] == "bb":
        res+='a'
        a-=1
    elif a>b:
        res+='a'
        a-=1
    else:
        res += 'b'
        b-=1
print(res)
# while a + b > 0:
#     if res[-2:] == "aa":
#         res += "b"
#         b -= 1
#     elif res[-2:] == "bb":
#         res += "a"
#         a -= 1
#     elif a > b:
#         res += "a"
#         a -= 1
#     else:
#         res += "b"
#         b -= 1
# print(res)