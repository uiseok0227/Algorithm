# 2178 미로탐색 
import sys
from collections import deque 

N,M = map(int,sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().strip())))

# BFS 
visited = [[0 for _ in range(M)] for _ in range(N)]
answer = 1 
deq = deque()
deq.append((0,0))
visited[0][0] = 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while(len(deq)):
    y,x = deq.popleft()
    for i in range(4):
        if(0<=y+dy[i]<N and 0<=x+dx[i]<M):
            if(visited[y+dy[i]][x+dx[i]] == 0 and board[y+dy[i]][x+dx[i]] !=0):
                visited[y+dy[i]][x+dx[i]] = visited[y][x]+1 
                deq.append((y+dy[i],x+dx[i]))

print(visited[N-1][M-1])