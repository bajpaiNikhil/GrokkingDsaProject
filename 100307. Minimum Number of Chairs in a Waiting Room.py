

s = "ELEELEELLL"
# d= {}
# for i in s:
#     d[i] = d.get(i,0)+1
# print(d)
entPep = 0
maxPep = 0

for i in s:
    if i == "E":
        entPep+=1
        maxPep = max(maxPep,entPep)
    else:
        entPep-=1
print(maxPep)