# 16236 아기상어


# 처음 아기상어 크기 2 / 1초에 상하좌우 인접하게 이동 / 자신의 크기보다 큰물고기가 있는 칸은 지나갈수 없음 / 크기와 같은수 먹으면 1증가 
# 지나갈수 있는지의 여부 판단 

# 아이디어 
# 먹을 수 있는 가까운 물고기 위치 파악하기 
# BFS로 이동거리 계산 -> 가능한 루트중 가장 짧은 루트로 / 지나갈수 없으면 엄마상어 

import sys 
from collections import deque 
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
shark_map = []
for i in range(N):
    shark_map.append(list(map(int,sys.stdin.readline().split())))

# 상어 현재 위치 파악하기 
for i in range(N):
    for j in range(N):
        if(shark_map[i][j] == 9):
            now_shark = [i,j]
            shark_map[i][j] = 0

# 더이상 먹을 수 있는 물고기가 공간에 있는지 없는지 파악하기
def check(shark_map,size):
    checking = False 
    for i in range(N):
        for j in range(N):
            if(0<shark_map[i][j]< size):
                checking = True 
    return checking 

# 상어 이동 
def bfs(shark_map,size,now_shark):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = []
    deq = deque()
    deq.append([now_shark,0])
    cand = []

    while(len(deq)):
        now = deq.popleft()
        if(now[0] not in visited):
            visited.append(now[0])
            for i in range(4):
                new_x = now[0][1] + dx[i]
                new_y = now[0][0] + dy[i]
                if(0<=new_x<N and 0<=new_y<N and shark_map[new_y][new_x]<=size):
                    if(0<shark_map[new_y][new_x] <size and [[new_y,new_x],now[1]+1] not in cand):
                        cand.append([[new_y,new_x],now[1]+1])
                    else:
                        deq.append([[new_y,new_x],now[1]+1])
    cand.sort(key= lambda x : (x[1],x[0][0],x[0][1]))

    return cand
            

result = 0 
size = 2 
eat_count = 0 
while(True):
    if(check(shark_map,size) == False):
        print(result)
        exit(0) 

    eat = bfs(shark_map,size,now_shark)
    if(len(eat) == 0):
        print(result)
        exit(0)
    eat = eat[0]
    shark_map[eat[0][0]][eat[0][1]] = 0
    now_shark = eat[0]
    eat_count += 1 
    if(eat_count == size):
        size+=1 
        eat_count = 0
    result+=eat[1]