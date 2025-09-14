import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
village = [0] + list(map(int, input().split()))
dp = [[None for _ in range(2)] for __ in range(N + 1)]
adjacent = [set() for _ in range(N + 1)] # adj[i] = adjacent village
for i in range(N - 1):
    a, b = map(int, input().split())
    adjacent[a].add(b)
    adjacent[b].add(a)

def req(tar, elite, parent):
    if dp[tar][elite] != None:
        return dp[tar][elite]
    
    dp[tar][elite] = 0

    if elite:
        for i in adjacent[tar]:
            if i != parent:
                dp[tar][elite] += req(i, 0, tar)
        dp[tar][elite] += village[tar]
    else:
        for i in adjacent[tar]:
            if i != parent:
                dp[tar][elite] += max(req(i, 0, tar), req(i, 1, tar))
    
    return dp[tar][elite]
print(max(req(1,0,0), req(1,1,0)))

#tree: no cycle, all connected
#dp[i] = max people in corrent depth





