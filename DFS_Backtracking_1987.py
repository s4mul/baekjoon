import sys
import heapq
input = sys.stdin.readline
movement = [(1,0),(0,1),(-1,0),(0,-1)]
res = 0
hashmap = [0 for ii in range(ord("A"),ord("Z") + 1)]



##x, y = a[x][y]
def trav(hashmap, cor_x, cor_y, board, cnt):
    global res
    flag = 0
    hashmap[board[cor_x][cor_y]] = 1
    res = max(cnt+1, res)
    print(hashmap)
    for xmove, ymove in movement:
        if 0 <= cor_x + xmove < len(board) and 0 <= cor_y+ymove < len(board[cor_x]) and hashmap[board[cor_x + xmove][cor_y+ymove]] == 0:
            trav(hashmap, cor_x + xmove, cor_y+ymove, board, cnt + 1)
            
    hashmap[board[cor_x][cor_y]] = 0 # recover hashmap

R, C = map(int, input().rstrip().split())
board = []

board = [list(map(lambda y: ord(y)-65,input().rstrip())) for i in range(R)]
trav(hashmap, 0, 0, board, 0)
print(res)
