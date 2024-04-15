

s = "xaxcd"
k = 4
ansList = list(s)
ans = ""
transformed_string = list(s)

for i in range(len(s)):
    current_distance_from_a = min(ord(s[i]) - ord('a'), 26 - (ord(s[i]) - ord('a')))
    if k >= current_distance_from_a:
        k -= current_distance_from_a
        transformed_string[i] = 'a'
    else:
        new_char_code = ord(s[i]) - k
        if new_char_code >= ord('a'):
            transformed_string[i] = chr(new_char_code)
        else:
            transformed_string[i] = chr(ord('z') - (k - 1))
        break

print("".join(transformed_string))
#
# for i in range(len(s)):
#     currentDistanceFromA= min(ord(s[i])-ord('a'),26-(ord(s[i])-ord('a')))
#     print(currentDistanceFromA)
#     if k >= currentDistanceFromA:
#         k-=currentDistanceFromA
#         ansList[i]='a'
#     else:
#         if k>0:
#             if ord(ansList[i])-k>=ord('a'):
#                 ansList[i] =chr(ord(ansList[i])-k)
#             else:
#                 ansList[i]=chr(ord('z')-(k-1))
#         break
# print("".join(ansList))
