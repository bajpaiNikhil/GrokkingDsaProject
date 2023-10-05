from collections import deque

dominoes = ".L.R...LR..L.."
# "LL.RR.LLRRLL.."
# ".............."
domino = list(dominoes)
q = deque()
for i, d in enumerate(domino):
    if d != ".":
        q.append((i, d))

while q:
    i, d = q.popleft()
    if d == "L" and domino[i - 1] == "." and i > 0:
        domino[i - 1] = "L"
        q.append((i - 1, "L"))
    elif d == "R":
        if i + 1 < len(domino) and domino[i + 1] == ".":
            if i + 2 < len(domino) and domino[i + 2] == "L":
                q.popleft()
            else:
                q.append((i + 1, "R"))
                domino[i + 1] = "R"
print(domino, "".join(domino))


print(13/2)
print(13/2.0)
print(13%2)
print(13%2.0)

num = 3+5*2%5-4
print(num)