

days = 10
meetings =   [[5,7],[1,3],[9,10]]
meetings.sort(key=lambda x:x[0])
mergeList = []
day = 0
for i in meetings:
    # if the list of merged intervals is empty
    # or if the current interval does not overlap with the previous,
    # simply append it.
    if not mergeList or mergeList[-1][-1] < i[0]:
        mergeList.append(i)
    else:
        mergeList[-1][-1] = max(mergeList[-1][-1], i[-1])
for i in mergeList:
    day += i[1]-i[0] +1
print(mergeList, days -day)
