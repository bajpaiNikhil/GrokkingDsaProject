strs = ["flower", "flow", "flight"]

# shortest = min(strs, key=len)
# for i, ch in enumerate(shortest):
#     for other in strs:
#         if other[i] != ch:
#             print(shortest[:i])
# print(shortest)

if len(strs) == 0:
    print("")
    exit()

prefix = strs[0]
for i in range(1,len(strs)):
    while strs[i].find(prefix) != 0:
        prefix = prefix[0:len(prefix)-1]
        print(prefix)
        if prefix == "":
            print("")
            exit()
print(prefix)
