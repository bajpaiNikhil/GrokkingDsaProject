position = [2,2,2,3,3]

oddCount = sum( i%2 for i in position)
evenCount = len(position)-oddCount
print(oddCount , evenCount)
print(min(oddCount,evenCount))