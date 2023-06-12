import math

blocks = "WBWW"
k = 2

count = math.inf
minCount = math.inf
for windowEnd in range(len(blocks)-k+1):
    print(blocks[windowEnd], windowEnd)
    blockIs = blocks[windowEnd:windowEnd+k]
    print(blockIs , blocks[windowEnd], windowEnd)
    count = blockIs.count("W")
    minCount =  min(count , minCount)
print(minCount)