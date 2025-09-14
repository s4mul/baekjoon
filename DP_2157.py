import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

graph = [[0 for _ in range(N + 1)] for __ in range(N + 1)]
dp = [[0 for _ in range(M + 1)] for __ in range(N + 1)] #값과 깊이

for i in range(K):
    a, b, c = map(int, input().split())
    if a < b:
        graph[a][b] = max(c, graph[a][b])

for i in range(2, N + 1):#1 -> N 직통
    dp[i][2] = graph[1][i]


for end in range(2, N + 1):
    for depth in range(3, M + 1):#중간에 한다리 거침 -> depth = 3
        for start in range(1, end):
            if graph[start][end] and dp[start][depth - 1]:
                dp[end][depth] = max(dp[end][depth], dp[start][depth - 1] + graph[start][end])
    
        
print(max(dp[N]))