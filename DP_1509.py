#in: string
#out: num of division of pellindrom
#
tar = input()
isp = [[0 for _ in range(len(tar))] for __ in range(len(tar))]
dp = [2501 for _ in range(len(tar) + 1)]

for i in range(len(tar)): #len 1
    isp[i][i] = 1

for i in range(len(tar) - 1):#len 2
    if tar[i] == tar[i + 1]:
        isp[i][i + 1] = 1


for l in range(3, len(tar) + 1):#len 3++
    for s in range(len(tar) - l + 1):  
        e = s + l - 1
        if tar[s] == tar[e] and isp[s + 1][e - 1]:
            isp[s][e] = 1

dp[-1] = 0
#[...s][...e]
for e in range(len(tar)):
    for s in range(e + 1):
        if isp[s][e] == 1:#[...] ([s...e]) = p -> [e] vs [s - 1] + 1
            dp[e] = min(dp[e], dp[s - 1] + 1)
        else:#[...][s...e] != p -> [e] vs [e - 1] + 1 ([...s...e-1][e]) 
            dp[e] = min(dp[e], dp[e - 1] + 1)


print(dp[-2])
