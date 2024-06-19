import math

prices = [7,5,4,1]
profit = 0
day = prices[0]
for i in range(1,len(prices)):
    diff = prices[i] - day
    profit = max(diff, profit)
    if diff <=0:
        day = prices[i]
print(profit)

