import sys
import heapq

INF = 1000000000
input = sys.stdin.readline

def dijkstra(N, start, adj):
    heap = [(0,start)]
    visited = [INF for _ in range(N + 1)]
    visited[start] = 0
    while heap:
        cor_c, cor_v = heapq.heappop(heap)
        if visited[cor_v] < cor_c:
            continue ## key point!
        for tar_v, tar_c in adj[cor_v]:
            cost = cor_c + tar_c
            if cost < visited[tar_v]:
                visited[tar_v] = cost
                heapq.heappush(heap,(cost, tar_v))
    return visited

N = int(input())

adj = [[] for _ in range(N+1)]

for ii in range(N - 1):
    s, e, c = map(int, input().rstrip().split())
    if s != e:
        adj[s].append((e,c))
        adj[e].append((s,c))
    
first = dijkstra(N, 1, adj)

maxIdx = 1
for ii in range(1,len(first)):
    if first[maxIdx] < first[ii]:
        maxIdx = ii
second = dijkstra(N, maxIdx, adj)

print(max(second[1:]))
