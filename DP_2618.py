import sys
input = sys.stdin.readline
INF = 100000000

N = int(input())
W = int(input())

ar = [tuple(map(int, input().split())) for _ in range(W)]
from_dp = [[None for _ in range(W + 1)] for __ in range(W + 1)]
dp = [[INF for _ in range(W + 1)] for __ in range(W + 1)]


def calcDist(car, cor):
    return abs(car[0] - cor[0]) + abs(car[1] - cor[1])

def getPos(idx, is_car1):
    if idx == 0:
        return (1, 1) if is_car1 else (N, N)
    return ar[idx - 1]

car1 = (0,0)
car2 = (N-1,N-1)

dp[0][0] = 0


for i in range(W + 1):
    for j in range(W + 1):
        if  i == j and i != 0:
            continue
        
        next_case = max(i, j) + 1
        
        if next_case > W:
            continue
                # 경찰차 1이 처리
        cost1 = dp[i][j] + calcDist(getPos(i, True), getPos(next_case, True))
        if dp[next_case][j] > cost1:
            dp[next_case][j] = cost1
            from_dp[next_case][j] = (i, j)
        
        # 경찰차 2가 처리
        cost2 = dp[i][j] + calcDist(getPos(j, False), getPos(next_case, False))
        if dp[i][next_case] > cost2:
            dp[i][next_case] = cost2
            from_dp[i][next_case] = (i, j)

# 최소값 및 끝 상태 추적
res = INF
end = (0, 0)
for i in range(W + 1):
    if dp[i][W] < res:
        res = dp[i][W]
        end = (i, W)
    if dp[W][i] < res:
        res = dp[W][i]
        end = (W, i)

print(res)

# 경로 역추적
route = []
x, y = end
for _ in range(W, 0, -1):
    prev = from_dp[x][y]
    if x != prev[0]:
        route.append(1)
    else:
        route.append(2)
    x, y = prev

route.reverse()
for r in route:
    print(r)