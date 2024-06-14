import sys 
from collections import deque

def outairfound(paper, melt, N, M, x, y):
    outair = deque([(x,y)])
    paper[x][y] = -1#외부공기는 -1
    direction = [(0,1),(1,0),(-1,0),(0,-1)]
    
    while outair: #외부공기랑 내부공기 파악
        x, y = outair.popleft()
        for dx, dy in direction:
            if 0 <= x+dx < N and 0<= y+dy < M:
                if paper[x+dx][y+dy] == 0:
                    paper[x+dx][y+dy] = -1
                    outair.append((x+dx, y+dy))
                    
                #동시에 1차적으로 외부공기에 노출된 횟수 조사; 값 - 1 = 노출된 횟수
                if paper[x+dx][y+dy] >= 1:
                    paper[x+dx][y+dy] += 1
                    
                if paper[x+dx][y+dy] == 3:#2면 이상 노출된 치즈 조사
                    melt.append((x+dx,y+dy))
                    paper[x+dx][y+dy] = -1 #이미 녹은 치즈; 중복된 검사를 막는다


N,M = map(int,sys.stdin.readline().rstrip().split())
paper = []
cheezes = 0
for i in range(N): #실제 배열 만들고 치즈 갯수 파악
    paper.append(list(map(int,sys.stdin.readline().rstrip().split())))
    cheezes += sum(paper[i])
    
melt = deque([])
outairfound(paper,melt,N,M,0,0)#외부공기를 파악하고 노출된 치즈를 녹인다.

#값이 녹은 치즈에 의해서만 바뀌므로 녹은 치즈에 대해서 조사를 시작
direction = [(0,1),(1,0),(-1,0),(0,-1)]
time = 0
while cheezes > 0:
    
    meltedcheezes = len(melt)
    for i in range(meltedcheezes):
        x, y = melt.popleft()
        for dx, dy in direction:
            if 0 <= x+dx < N and 0<= y+dy < M:
                if paper[x+dx][y+dy] >= 1: #새로 노출된 치즈 조사
                    paper[x+dx][y+dy] += 1
                    
                if paper[x+dx][y+dy] == 0:#내부공기 노출여부 조사
                    outairfound(paper, melt, N, M, x+dx, y+dy)
                    
                if paper[x+dx][y+dy] == 3:#2면이 노출되었을때 녹음; 같은 치즈가 여러번 대상에 추가되는거 방지
                    melt.append((x+dx,y+dy))
                    paper[x+dx][y+dy] = -1#치즈는 녹았지만 녹은 부분에 대한 처리는 다음 회차에
    time += 1

    cheezes -= meltedcheezes
                    
print(time)

