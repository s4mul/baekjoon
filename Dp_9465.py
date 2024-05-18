import sys

sticker = []
T = int(sys.stdin.readline())


for i in range(T):
    N = int(sys.stdin.readline())
    sticker = []
    sticker.append(list(map(int,sys.stdin.readline().split())))
    sticker.append(list(map(int,sys.stdin.readline().split())))
    if N == 1:
        sys.stdout.write(str(max(sticker[0][0], sticker[1][0])+"\n"))
    if N == 2:
        sys.stdout.write(str(max(sticker[0][0] + sticker[1][1],sticker[1][0] + sticker[0][1])+"\n"))
        
    Max = 0
    for i in range(2, N):
        sticker[0][i] = sticker[0][i]+max(sticker[0][i - 2] + sticker[1][i - 1], sticker[1][i - 2])
        sticker[1][i] = sticker[1][i]+max(sticker[1][i - 2] + sticker[0][i - 1], sticker[0][i - 2])
        print(sticker[0])
        print(sticker[1])
        print()
        Max = max(sticker[0][i], sticker[1][i], Max)
        
    sys.stdout.write(str(Max)+"\n")
    
