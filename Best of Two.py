t = int(input())
for t in range(t):
    l = list(map(int, input().split()))
    alice = l[:3]
    bob = l[3:]
    alice.sort(reverse=True)
    bob.sort(reverse=True)
    aliceSum = alice[0] + alice[1]
    bobSum = bob[0] + bob[1]
    print(alice ,bob ,aliceSum,bobSum)
    if aliceSum > bobSum:
        print("Alice")
    if bobSum > aliceSum:
        print("Bob")
    if aliceSum == bobSum:
        print("Tie")