import sys


n, k = map(int,sys.stdin.readline().rstrip().split())
coin = [(lambda x : int(sys.stdin.readline().rstrip()))(_) for _ in range(n)]
dp = [0 for __ in range(k+1)]

dp[0] = 1
idx = 0
for coinValue in coin:
    for i in range(coinValue, k+1):
        dp[i] += dp[i - coinValue]
    print(dp)
    
print(dp[k])
