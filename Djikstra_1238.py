# input: student N edge M point x
# output: Max length student
# find length all student
# time limit: 1sec, NM = 10000000(0.1sec)
# conditions: tree, all connected

# idea: start X and Dijkstra, find all weight
#       use Dijkstra alg to find way reach X
import sys
import heapq as h
class graph:
    def __init__(self, V):
        self.node = [[] for _ in range(V)]
    
    def addEdge(self, start, end, weight): #V = 0, 1, 2, 3
        self.node[start].append([end,weight])
#class graph
    

def build_tree(V, E) -> graph:
    tree = graph(V)
    for i in range(E):
        data = sys.stdin.readline().rstrip()
        data = list(map(int,data.split()))

        tree.addEdge(data[0] - 1, data[1] - 1, data[2])# V = 1,2,3
    return tree

def Dijkstra(street, X) -> list:
    queue = []
    h.heappush(queue, (1,X - 1))

    visited = [0 for _ in range(len(street.node))]
    visited[X - 1] = 1
    while len(queue) > idx:
        cor = h.heappop(queue)
        
        for ii in street.node[cor[1]]:
            if visited == 0 or visited[cor]:
            visited[ii[0]] = visited[cor] + ii[1]
            queue.append(ii[0])
    
    return visited
    
N, M , X = map(int,sys.stdin.readline().rstrip().split())
street = build_tree(N,M)
print(street.node)
res = BFS(street, X)
print(res)
