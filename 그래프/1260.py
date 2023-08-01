# 1260 DFS와 BFS
import sys 
from collections import deque
N,M,V = map(int,sys.stdin.readline().split())
info = [[] for _ in range(N+1)]
for i in range(M):
    n_from,n_to = map(int,sys.stdin.readline().split())
    info[n_from].append(n_to)
    info[n_to].append(n_from)

global visited
visited = [V]

def DFS(v,vistied):
    global visited
    nodes = info[v]
    nodes.sort()
    for node in nodes:
        if(node not in visited):
            visited.append(node)
            DFS(node,visited)

# DFS
DFS(V,visited)
print(str(visited).replace("[","").replace("]","").replace(",",""))

# BFS 
visited = [V]
deq = deque()
deq.append(V)
while(len(deq)):
    now = deq.popleft()
    nodes = info[now]
    nodes.sort()
    for node in nodes:
        if(node not in visited):
            deq.append(node)
            visited.append(node)
print(str(visited).replace("[","").replace("]","").replace(",",""))