#in                     out
#T: testcase            min time to victort structure
#N: num of structure
#D1 D2 .. DN = time
# X Y: X -> Y
#W = victory structure
import sys
from collections import deque
import heapq
input = sys.stdin.readline



T = int(input())

for __ in range(T):
    N, K = map(int,input().split())
    D = [0]+list(map(int,input().split()))
    build = [[] for _ in range(N+1)]#idjacent list
    buildRequire = [[] for _ in range(N+1)]#Collection of structure needed to build
    income = [0 for _ in range(N+1)]
    time = [0 for _ in range(N+1)]
    income[0] = -1
    for _ in range(K):
        x, y = map(int,input().split())
        build[x].append(y)
        buildRequire[y].append(x)
        income[y] += 1
    W = int(input())
    
    topsorted = []
    done = 0
    while done < N:#topologe sort
        leaf = []
        for i in range(N+1): # income rate = 0 node collect
            if income[i] == 0:
                income[i] = -1
                done += 1
                leaf.append(i)
                
                
        for i in leaf: #reflect change
            for j in build[i]:
                income[j] -= 1
        
        if leaf:# add topologe
            topsorted.append(leaf)

        
    for topologe in topsorted:#each level
        for j in range(len(topologe)):# each node
            tmp = [0]# a -> a
            for req in buildRequire[topologe[j]]:
                tmp.append(time[req])
            time[topologe[j]] = D[topologe[j]] + max(tmp)
    print(time[W])
