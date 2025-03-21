word = "abbcccc"
# n = len(word)
# firstWord = word[0]
# count = 0
# for i in range(1,n):
#     if firstWord == word[i]:
#         count+=1
#         firstWord = word[i]
# print(count)
count = 0
lastElement = word[0]
for i in range(1,len(word)):
    print("OutSide loop", lastElement, word[i], count)

    if lastElement == word[i]:
        print("withIn loop",lastElement,word[i],count)
        count+=1
    lastElement = word[i]
print(count+1)