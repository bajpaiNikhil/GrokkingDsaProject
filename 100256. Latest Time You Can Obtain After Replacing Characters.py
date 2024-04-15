s = "1?:??"
s = list(s)
#
# if s[0] == "?":
#     if s[1] == "?" or s[1] < "2":
#         s[0] = "1"
#     else:
#         s[0] = "0"
# if s[1] == "?":
#     if s[0] == "1":
#         s[1] = "1"
#     else:
#         s[1] = "9"
# if s[3] == "?":
#     s[3] = "5"
# if s[4] == "?":
#     s[4] = 9
if s[0] == "?":
    s[0] = "1" if s[1] == "?" or s[1] < "2" else "0"

# Handle the second character
if s[1] == "?":
    s[1] = "1" if s[0] == "1" else "9"

# Handle other question marks
s[3] = "5" if s[3] == "?" else s[3]
s[4] = "9" if s[4] == "?" else s[4]

print("".join(s))
