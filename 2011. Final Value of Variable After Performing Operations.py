operations = ["++X","++X","X++"]
op_dict = {"--X" : -1, "X--" : -1,
                 "++X" : 1, "X++" : 1}

ans = 0
for i in operations:
    ans+=op_dict[i]
print(ans)