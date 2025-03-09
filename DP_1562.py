import sys
input = sys.stdin.readline

N = int(input())

dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N)]

for i in range(1,10):
    dp[0][i][1 << (i)] = 1


for i in range(1,N):
    for j in range(10):
        for k in range(1024):
            
            if j > 0:
                dp[i][j][k | (1 << (j))] += dp[i - 1][j - 1][k]
            if j < 9:
                dp[i][j][k | (1 << (j))] += dp[i - 1][j + 1][k]
                
            dp[i][j][k | (1 << j)] %= 1000000000

Sum = 0

for j in range(10):  # 마지막으로 도착한 숫자 (0~9)
    Sum += dp[N - 1][j][1023]  # 0부터 9까지 모든 숫자를 방문했을 때, 1111111111(2) = 1023
    Sum %= 1000000000

print("S:", Sum)

