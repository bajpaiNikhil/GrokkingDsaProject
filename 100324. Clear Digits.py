
s = "cb34" #a

stack = []
for i in s:
    if i.isdigit() and len(stack)>0:
        stack.pop()
    if i.isalpha():
        stack.append(i)
print("".join(stack))