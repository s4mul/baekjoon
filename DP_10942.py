import sys
input = sys.stdin.readline
N = int(input())

tar = list(map(int, input().split()))
print(tar)
M = int(input())

isp = [[0 for _ in range(len(tar))] for __ in range(len(tar))]

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

for i in range(M):
    S, E = map(int, input().split())
    print(isp[S - 1][E - 1])

