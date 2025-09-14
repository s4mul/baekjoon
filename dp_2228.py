import sys
input = sys.stdin.readline
INF = -100000000000000


N, M = map(int, input().split())
accumulatedarray = []
dp = [[INF for _ in range(M+1)] for __ in range(N+1)]
dp[0][0] = 0
accumulatedarray.append(0)
for i in range(N):
    accumulatedarray.append(accumulatedarray[-1] + int(input()))

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i - 1][j]
        for k in range(1, i+1):
            range_sum = accumulatedarray[i] - accumulatedarray[k - 1]
            
            if j == 1:
                dp[i][j] = max(dp[i][j], range_sum)
                
            elif k - 2 >= 0 and dp[k - 2][j - 1] != INF:
                dp[i][j] = max(dp[i][j], dp[k - 2][j - 1] + range_sum)

result = INF
for i in range(1, N+1):
    result = max(result, dp[i][M])
print(result)