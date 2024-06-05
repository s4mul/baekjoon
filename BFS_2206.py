import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
#arr[N][M]
bitmap = [[],[]]
bitmap[0] = [list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(N)]
bitmap[1] = [[0 for __ in range(M)] for _ in range(N)]


movement = [(1,0),(-1,0),(0,1),(0,-1)]
queue = deque([]) #x, y, broken
queue.appendleft((0,0,0))
bitmap[0][0][0] = 2 # start point = 2, divided with 0,1
idx = 0

while queue:
    broken, x, y= queue.pop()
    if x == N-1 and y == M - 1:
        ans = bitmap[broken][x][y] -1
        break
    
    for dx, dy in movement:
        if 0<= x + dx < N and 0 <= y + dy < M:
            
            if broken == 0 and bitmap[broken][x+dx][y+dy] == 1:
                bitmap[1][x+dx][y+dy] = bitmap[0][x][y] + 1
                queue.appendleft((1,x+dx,y+dy))
                
            elif bitmap[broken][x+dx][y+dy] == 0 and bitmap[0][x+dx][y+dy] == 0:
                bitmap[broken][x+dx][y+dy] = bitmap[broken][x][y] + 1
                
                queue.appendleft((broken,x+dx,y+dy))
    ans = -1

print(ans)
