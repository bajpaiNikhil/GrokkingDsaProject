
prices = [7, 1, 5, 3, 6, 4]
profit = 0
day = prices[0]
finalProfit = 0
for i in range(1,len(prices)):
    diff = prices[i]-day
    print("day", diff,prices[i],day,profit)
    profit = max(profit,diff)
    if diff<=0:
        day = prices[i]

print(profit)
