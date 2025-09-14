N = int(input())
l, r = map(int,input().split())
T = int(input())
INF = 10000000
dp = [[[INF for _ in range(N + 1)] for __ in range(N + 1)] for ___ in range(T + 1)]
seq = []
l, r = min(l, r), max(l,r) 
#dp[0][l][r] = 0
for i in range(T):
    seq.append(int(input()))
seq.append(0)
def req(step, l, r):
    if step == T:
        return 0
    if dp[step][l][r] != INF:
        return dp[step][l][r]
    t = seq[step]

    move_left = abs(t - l) + req(step + 1, t, r)
    move_right = abs(t - r) + req(step + 1, l, t)
    dp[step][l][r] = min(move_left, move_right)

    return dp[step][l][r]
print(req(0, l, r))

