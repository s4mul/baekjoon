import sys
input = sys.stdin.readline
N = int(input())
maxpoint = [0,0,0]
minpoint = [0,0,0]

for ii in range(N):
    score = list(map(int, input().rstrip().split()))
    tmp = [max(maxpoint[:2]) + score[0],max(maxpoint) + score[1],max(maxpoint[1:]) + score[2]]
    # left
    maxpoint[0] = tmp[0]
    #mid
    maxpoint[1] = tmp[1]
    #right
    maxpoint[2] = tmp[2]
    
    
    tmp = [min(minpoint[:2]) + score[0],min(minpoint) + score[1],min(minpoint[1:]) + score[2]]
     # left
    minpoint[0] =tmp[0]
    #mid
    minpoint[1] =tmp[1]
    #right
    minpoint[2] =tmp[2]

print(max(maxpoint), min(minpoint))
