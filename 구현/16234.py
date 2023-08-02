# 16234 인구 이동

# 두 나라의 인구차이가 L<= <=R 면 국경선 연다 
# 국경선 열려있는경우 연합 
# 연합을 이루고 있는 각칸의 인구수는 연합의 인구수/연합 칸

# 아이디어
# 열결된 곳 표시 
# BFS 로 열린 구역 파악 
# 인원 분배 

import sys 
from collections import deque

N,L,R = map(int,sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))


# 이동 가능 여부 확인 함수 + 연결된 국경 딕셔너리로 반환. 시간 이내 
def check(board):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    open_gate = dict()
    for y in range(N):
        for x in range(N):
            for d in range(4):
                if(0<=y+dy[d]<N and 0<=x+dx[d]<N and L<=abs(board[y][x] - board[y+dy[d]][x+dx[d]])<=R):
                    try:
                        open_gate[(y,x)].append((y+dy[d],x+dx[d]))
                    except:
                        open_gate[(y,x)] = [(y+dy[d],x+dx[d])]
    
    return open_gate

# BFS 
def bfs(start,gates):
    global visited
    result = []
    if(visited[start[0]][start[1]] == False):
        visited[start[0]][start[1]] = True
        result.append(start)
        deq = deque()
        deq.append(start)
        while(len(deq)):
            now = deq.popleft()
            try:nodes = gates[now]
            except:nodes = []
            for node in nodes:
                if(visited[node[0]][node[1]] == False):
                    visited[node[0]][node[1]] = True
                    result.append(node)
                    deq.append(node)
    return result 

result = 0
while(True):
    gates = check(board)
    if(len(gates.keys()) == 0):
        print(result)
        exit(0)
    global visited 
    visited = [[False for _ in range(N)] for _ in range(N)]
    connections = []
    for i in range(N):
        for j in range(N):
            connection = bfs((i,j),gates)
            if(len(connection)>1):connections.append(connection)
    for conn in connections:
        sum_conn = 0
        for country in conn:
            sum_conn+=board[country[0]][country[1]]
        people = sum_conn // len(conn)
        for country in conn:
            board[country[0]][country[1]] = people 
    result += 1 