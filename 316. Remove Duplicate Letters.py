
s = "cbacdcbc"

seen = set()
stack = []
lastOccurrence = {c:i for i,c in enumerate(s)}
print(lastOccurrence)

for i,c in enumerate(s):
    # print(i,c)
    if c not in seen:
        while stack and c <stack[-1] and i<lastOccurrence[stack[-1]]:
            seen.remove(stack.pop())
        seen.add(c)
        stack.append(c)
print("".join(stack))
