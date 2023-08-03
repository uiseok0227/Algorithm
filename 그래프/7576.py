# 7576 토마토
# BFS를 이용해서 토마토가 익는걸 만들기
# check함수 구현 시 처음부터 토마토 없는 경우 생각 
# 토마토가 모두 익지 못하는 상태 구현? 
import sys 
from copy import deepcopy
from collections import deque 
M,N = map(int,sys.stdin.readline().split())
board = []
for n in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

deq = deque()
visited = [[-1 for _ in range(M)] for _ in range(N)] 
for i in range(N):
    for j in range(M):
        if(board[i][j] == 1):
            deq.append((i,j))
            visited[i][j] = 0
            
        elif(board[i][j] == -1):
            visited[i][j] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]
while(len(deq)):
    y,x = deq.popleft()
    for d in range(4):
        ny,nx = y+dy[d],x+dx[d]
        if(0<=ny<N and 0<=nx<M and visited[ny][nx]==-1 and board[ny][nx]==0):
            visited[ny][nx] = visited[y][x]+1
            deq.append((ny,nx))
min_num = 10000000000 
max_num = -100000000
for b in visited:
    max_num = max(max(b),max_num)
    min_num = min(min(b),min_num)

if(min_num <0):
    print(-1)
else:
    print(max_num)

# # check 함수. 
# def check():
#     # 모든 토마토가 익은 상태: 0이 없으면 다 익은 상태 
#     for i in range(N):
#         for j in range(M):
#             if(board[i][j]==0):
#                 return False 
#     return True 

# day = 0 
# while(True):
#     if(check() == True):
#         print(day)
#         exit(0)

#     temp_board = deepcopy(board)
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]

#     for i in range(N):
#         for j in range(M):
#             if(board[i][j] == 1):
#                 for d in range(4):
#                     ny,nx = i+dy[d],j+dx[d]
#                     if(0<=ny<N and 0<=nx<M and board[ny][nx] == 0):
#                         temp_board[ny][nx] = 1 
#     if(temp_board == board):
#         print(-1)
#         exit(0)
#     board = temp_board
#     day+=1 
