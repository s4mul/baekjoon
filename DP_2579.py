N = int(input())
dp = [0 for _ in range(N + 3)]#padding
step = []

for _ in range(N):
    step.append(int(input()))
step += [0, 0]#padding


dp[0] = step[0]
dp[1] = step[0] + step[1]

for i in range(2, N):
    dp[i] = max(dp[i - 2] + step[i], dp[i - 3] + step[i - 1] + step[i])

print(dp[N - 1])