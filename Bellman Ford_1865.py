#in: graph
#out: find negative edge with any start point

#same edge not same weight = True
#max edge = 2700 max V^2 = 250000, maxWeight = 5000000
#adj list + hash map

import sys
input = sys.stdin.readline
INF = 10000000
tc = int(input())



for i in range(tc):
    N, M, W = map(int,input().split())
    
    adj = [[INF for _ in range(N+1)] for __ in range(N+1)]
    edge = [[] for _ in range(N+1)]
    
    for jj in range(M): #build road
        s, e, t =  map(int,input().split())
        if adj[s][e] > t:#better root
            if adj[s][e] == INF:#first root
                edge[s].append(e)
            adj[s][e] = t
            

        if adj[e][s] > t:#bothways
            if adj[e][s] == INF:
                edge[e].append(s)
            adj[e][s] = t
            
                
    for jj in range(W):
        s, e, t =  map(int,input().split())
        t *= -1#time reap
        if adj[s][e] > t:#better root, oneway
            if adj[s][e] == INF:#first root
                edge[s].append(e)
            adj[s][e] = t
            
    ##build graph
    idx = 0
    time = [INF for _ in range(N + 1)]
    time[1] = 0
    
    change = 0
    for jj in range(N):
        change = 0
        for start_v in range(1, N + 1):
            for reach in edge[start_v]:
                if time[reach] > time[start_v] + adj[start_v][reach]:
                    time[reach] = time[start_v] + adj[start_v][reach]
                    change = 1
        if change == 0:
            break
    if change == 1:
        print("YES")
    else:
        print("NO")
