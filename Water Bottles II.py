numBottles = 13
numExchange = 6


drunkBottle = numBottles

emptyBottles = numBottles
numBottles = 0
while emptyBottles >= numExchange:
    emptyBottles-= numExchange
    drunkBottle+=1
    numExchange+=1
    emptyBottles+=1
print(drunkBottle)