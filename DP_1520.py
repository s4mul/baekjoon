#in: N*M arr
#out: num of route to reach arr[N,M]

def trev(x, y, N, M, direction, ar, dp, visit):

    if visit[y][x] == 1:
        return dp[y][x]
    else:
        visit[y][x] = 1
        for dx, dy in direction:
            if 0 <= x + dx < M and 0 <= y + dy < N and ar[y][x] > ar[y + dy][x + dx]:
                dp[y][x] += trev(x+dx, y+dy,N,M, direction, ar, dp, visit)
        return dp[y][x]

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N, M = map(int, input().rstrip().split())
ar = []
dp = []
visit = []
direction = [(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(N):
    ar.append(list(map(int, input().rstrip().split())))
    dp.append([0 for _ in range(M)])
    visit.append([0 for _ in range(M)])
dp[-1][-1] = 1
trev(0,0,N,M,direction,ar,dp,visit)

print(dp[0][0])
