

citations = [3,0,6,1,5]
n = len(citations)
paperCount = [0]*(n+1)
print(paperCount)
for c in citations:
    paperCount[min(c,n)]+=1
print(paperCount)
h = n
papers = paperCount[n]
print(papers)
while papers<h:
    h -=1
    print(h)
    papers+=paperCount[h]
    print(papers)
print(h)