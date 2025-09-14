n, k = map(int,input().split())

bud = [(0,0)]
for i in range(n):
    w, v = map(int,input().split())
    bud.append((w,v))

dp = [[0 for _ in range(n + 1)] for __ in range(k+1)]
# ➡ maxvalue    ️⬇weight

for i in range(1, k + 1):
    for j in range(1, n + 1):
        if i - bud[j][0] >= 0:#최대 무게보다 작을때, 즉 넣을 수 있을 때
            dp[i][j] = max(dp[i][j-1], dp[i - bud[j][0]][j - 1] + bud[j][1])
        else:
            dp[i][j] = dp[i][j-1]


print(dp[-1][-1])