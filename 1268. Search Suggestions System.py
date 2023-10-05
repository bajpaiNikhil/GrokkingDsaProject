products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"

products.sort()
left = 0
right = len(products) - 1
result = []
for index, character in enumerate(searchWord):
    # print(index,character)
    while left <= right and (len(products[left]) < index or products[left][index] != character):
        left += 1
    while left <= right and (len(products[right]) < index or products[right][index] != character):
        right -= 1
    result.append([])
    remaining = right - left +1
    for characterToAdd in range(min(3,remaining)):
        result[-1].append(products[left+characterToAdd])
print(result)
