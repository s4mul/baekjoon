import sys

sticker = []
T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    sticker = []
    sticker.append(list(map(int,sys.stdin.readline().split())))
    sticker.append(list(map(int,sys.stdin.readline().split())))
    DP = [[0 for _ in range(N)],[0 for _ in range(N)]]
    
    
    
    if N == 1:
        sys.stdout.write(str(max(sticker[0][0], sticker[1][0]))+"\n")
        continue
        
    elif N == 2:
        sys.stdout.write(str(max(sticker[0][0] + sticker[1][1],sticker[1][0] + sticker[0][1]))+"\n")
        continue
    else:
        DP[0][0] = sticker[0][0]
        DP[1][0] = sticker[1][0]
        DP[0][1] = DP[1][0] + sticker[0][1]
        DP[1][1] = DP[0][0] + sticker[1][1]
        
    Max = 0
    for i in range(2, N):
        DP[0][i] = max(DP[1][i - 1], DP[1][i - 2]) + sticker[0][i]
        DP[1][i] = max(DP[0][i - 1], DP[0][i - 2]) + sticker[1][i]
        

        
    sys.stdout.write(str(max(DP[0][-1],DP[1][-1]))+"\n")
    
