#in
#N: number of jewel
#K: number of bag
#M, V: weight/value of jewel
#Ci: max weight of bag

#out: max price of jewels

import heapq
import sys
input = sys.stdin.readline


N, K = map(int, input().rstrip().split())
jewels = []
bags = []

for i in range(N):
    M, V = map(int, input().rstrip().split())
    jewels.append((M,V))
    
for i in range(K):
    bags.append(int(input().rstrip()))

bags = sorted(bags, reverse = False)
jewels = sorted(jewels, reverse = False, key = lambda x : x[0])
ableJewels = []

idx = 0
ans = 0
for bag in bags:
    while idx < N and jewels[idx][0] <= bag:
        heapq.heappush(ableJewels,-1 * jewels[idx][1])
        idx += 1
    if ableJewels:
        ans -= heapq.heappop(ableJewels)


print(ans)
