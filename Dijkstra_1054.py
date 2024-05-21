#1 - a - b - N
# 1 - a - b - N
# N - a - b - 1
# in case a == 1 or N, b == 1 or N:
# weight of (a - 1, a - N, b - 1, b - N ) is 0. so no need to branch processing.

import sys
import heapq
input = sys.stdin.readline
INF = 1000000000
def dij(idj, start): #dijkstra alg
    visited = [INF for _ in range(N+1)]r
    heap = [(0,start)]
    visited[start] = 0
    
    while heap:
      
        cor_w, cor_v = heapq.heappop(heap)
        for  edge, weight in idj[cor_v]:
            if visited[edge] > cor_w + weight:
                visited[edge] = cor_w + weight
                heapq.heappush(heap, (visited[edge], edge))
        
    return visited
    


N, E= map(int, input().split())

idj = [[] for _ in range(N+1)]

for ii in range(E):
    s, e, w = map(int, input().split())
    idj[s].append((e,w))
    idj[e].append((s,w))

a,b = map(int, input().split())

weightarr_1 = dij(idj,1)
weightarr_N = dij(idj, N)
dist_ab = dij(idj,a)[b]
dist_1a = weightarr_1[a]
dist_1b = weightarr_1[b]
dist_Nb = weightarr_N[b]
dist_Na = weightarr_N[a]

res = dist_ab+min(dist_1a+dist_Nb, dist_1b+dist_Na) # 1 - a - b - N or 1 - b - a - N
if res >= INF: #can't reach
    print(-1)
else:
    print(res)
