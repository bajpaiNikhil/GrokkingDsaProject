s = "abc"
t = "bac"
distance = 0
for i in s:
    distance+=(abs(s.index(i) - t.index(i)))
print(distance)