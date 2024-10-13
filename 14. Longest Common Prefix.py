strs = ["flower", "flow", "flight"]

shortest = min(strs, key=len)
for i, ch in enumerate(shortest):
    for other in strs:
        if other[i] != ch:
            print(shortest[:i])
print(shortest)