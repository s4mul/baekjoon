import sys
import heapq

INF = 1000000000
input = sys.stdin.readline

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]

for ii in range(M):
    s, e, c = map(int, input().rstrip().split())
    if s != e:
        adj[s].append((e,c))
    
start, end = map(int,input().rstrip().split())


heap = [(0,start)]
visited = [INF for _ in range(N + 1)]

while heap:
    cor_c, cor_v = heapq.heappop(heap)
    if visited[cor_v] < cor_c:
        continue ## key point!
    for tar_v, tar_c in adj[cor_v]:
        cost = cor_c + tar_c
        if cost < visited[tar_v]:
            visited[tar_v] = cost
            heapq.heappush(heap,(cost, tar_v))

print(visited[end])
    
