import sys
from collections import deque
movement = [(1,0),(-1,0),(0,1),(0,-1)]
def trev(x, y, bitmap, movement, mode):
    queue = deque([]) #x, y, broken
    queue.appendleft((x,y))
    bitmap[x][y] = 2 * mode # start point = 2, divided with 0,1
    
    while queue:
        x, y= queue.pop()
        for dx, dy in movement:
            if 0<= x + dx < N and 0 <= y + dy < M:
                if bitmap[x+dx][y+dy] == 0:
                    bitmap[x+dx][y+dy] = bitmap[x][y] + mode
                    queue.appendleft((x+dx,y+dy))
    return (x,y)

N, M = map(int, sys.stdin.readline().rstrip().split())
#arr[N][M]
bitmap = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]

shortcut = []

if trev(0, 0, bitmap, movement,1) != (N-1, M-1):#cant reach endpoint
    trev(N-1,M-1,bitmap,movement,-1)#reverse search
    for x in range(N):
        for y in range(M):
            if bitmap[x][y] == 1:
                flag = [10000000,-10000000]
                for dx, dy in movement:
                    if 0<= x + dx < N and 0 <= y + dy < M:
                        if bitmap[x+dx][y+dy] > 1 and bitmap[x+dx][y+dy] < flag[0]:
                            flag[0] = bitmap[x+dx][y+dy]
                        elif bitmap[x+dx][y+dy] < 0 and bitmap[x+dx][y+dy] > flag[1]:
                            flag[1] = bitmap[x+dx][y+dy]
                if flag[0] != 10000000 and flag[1] != -10000000:
                    shortcut.append(flag[0] - flag[1] -1)
    if len(shortcut) > 0:
        print(min(shortcut))
    else:
        print(-1)
else:
    shortcut.append(0)
    for x in range(N):#can reach endpoint
        for y in range(M):
            if bitmap[x][y] == 1:
                near = []
                for dx, dy in movement:
                    if 0<= x + dx < N and 0 <= y + dy < M and (bitmap[x+dx][y+dy] != 0 and bitmap[x+dx][y+dy] != 1):
                        near.append(bitmap[x+dx][y+dy])
                if len(near) >= 2:
                    shortcut.append(max(near) - min(near) - 2)
    
    print(bitmap[-1][-1] - max(shortcut)-1)
