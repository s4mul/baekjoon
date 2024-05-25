import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
#arr[N][M]
bitmap = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
#bitmap = [list(map(lambda x: [int(x),0],list(sys.stdin.readline().rstrip()))) for _ in range(N)]
movement = [(1,0),(-1,0),(0,1),(0,-1)]
queue = deque([]) #x, y, broken
queue.appendleft((0,0,0))
bitmap[0][0][0] = 2 # start point = 2, divided with 0,1
idx = 0

while queue:
    x, y, broken = queue.pop()
   
    for dx, dy in movement:
        if 0<= x + dx < N and 0 <= y + dy < M:
            if bitmap[x+dx][y+dy][0] == 0 or bitmap[x+dx][y+dy][0] >= bitmap[x][y][0] + 1 and bitmap[x+dx][y+dy][1] == 0:
                bitmap[x+dx][y+dy][0] = bitmap[x][y][0] + 1
                bitmap[x+dx][y+dy][1] = 0
                queue.appendleft((x+dx,y+dy,broken))
            elif broken == 0 and bitmap[x+dx][y+dy][0] == 1:
                bitmap[x+dx][y+dy][0] = bitmap[x][y][0] + 1
                bitmap[x+dx][y+dy][1] = 1
                queue.appendleft((x+dx,y+dy,1))
print(bitmap[N-1][M-1][0]-1)
