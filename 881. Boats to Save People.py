
people = [1, 1, 2, 3, 9, 10, 11, 12]
people.sort()
limit = 12
left = 0
right = len(people)-1
boat = 0
while left<right:
    if people[left]+people[right] <= limit:
        left+=1
        right -=1
    else:
        right-=1
    boat+=1
print(boat)