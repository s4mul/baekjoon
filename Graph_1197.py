import sys
input = sys.stdin.readline

V, E  = map(int, input().split())
vertex = [0 for _ in range(V+1)]
edge = []

for i in range(E):
    A, B, W = map(int, input().split())
    edge.append((W,A,B))

    
#kruskal
def root(i, union):
    if union[i] == i:
        return i
    else:
        i = union[i]
        return root(i,union)

def merge(i, j, union):
    master = root(i,union)
    slave = root(j,union)
    if master < slave:
        master, slave = slave, master
    union[slave] = master

union = [i for i in range(V+1)]

edge.sort()
visited = [0 for _ in range(V+1)]
visit = 1
totalWeight = 0
idx = 0
while visit < V:
    
    w,a,b = edge[idx]
    a = root(a,union)
    b = root(b,union)
    if a != b:
        merge(a,b,union)
        visit += 1
        totalWeight += w
    idx += 1

print(totalWeight)
