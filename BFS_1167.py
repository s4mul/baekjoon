import sys

class graph:
    def __init__(self, V):
        self.node = [[] for _ in range(V)]
    
    def addEdge(self, start, end, weight): #V = 0, 1, 2, 3
        self.node[start].append([end,weight])
#class graph
    

def build_tree(V) -> graph:
    tree = graph(V)
    for i in range(V):
        data = sys.stdin.readline().rstrip()
        data = list(map(int,data.split()))
        
        for jj in range(1, len(data), 2):
            if data[jj] == -1:
                break
            tree.addEdge(data[0] - 1, data[jj] - 1, data[jj+1])# V = 1,2,3
    return tree

def BFS(tree, V, startNode) -> int: #return max length node
    visited = [0 for _ in range(V)]
    visited[startNode] = 1
    queue = [startNode]
    idx = 0
    while idx < len(queue):
        correntNode = queue[idx]
        idx += 1
        for i in tree.node[correntNode]:
            if visited[i[0]] == 0:
                queue.append(i[0])
                visited[i[0]] = visited[correntNode] + i[1]
    
    Max = 0
    for i in range(V):
        if visited[i] > visited[Max]:
            Max = i
            
    return [Max, visited[Max] - 1]
    
def diameter_tree(tree, V) -> int:
    diameterStartNode = BFS(tree, V, 0)[0]
    return BFS(tree, V, diameterStartNode)[1]


V = int(sys.stdin.readline().rstrip())
tree = build_tree(V)
sys.stdout.write(str(diameter_tree(tree,V)))
