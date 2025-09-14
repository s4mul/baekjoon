N = int(input())
point = list(map(int, input().split()))

dp = [0 for _ in range(N+1)]

for i in range(N + 1):
    M = m = point[i - 1]
    for j in range(i-1, -1, -1):
        M = max(M, point[j])
        m = min(m, point[j])
        dp[i] = max(dp[i], M - m + dp[j]) 
   
print(dp[N])

