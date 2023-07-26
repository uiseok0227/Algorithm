# 17144 미세먼지 안녕! 

# 아이디어 
# 그냥 문제의 조건대로 함수를 만들고 구현 

import sys 
from copy import deepcopy

R,C,T = map(int,sys.stdin.readline().split())

air_map = []
for i in range(R):
    air_map.append(list(map(int,sys.stdin.readline().split())))

# 0.공기청정기 위치 확인. 0번째가 위에거 1번째가 밑에거 
air = []
for i in range(R):
    for j in range(C):
        if(air_map[i][j] == -1):
            air.append([i,j])

# 1.확산
def spread(air_map):
    plus_list = [[0 for _ in range(C)] for _ in range(R)]
    minus_list = [[0 for _ in range(C)] for _ in range(R)]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(R):
        for j in range(C):
            if(air_map[i][j] >0):
                count = 0
                direction = []
                for d in range(4):
                    # 몇방향으로 퍼질 수 있는지 확인해야함 
                    # 퍼질수 없는 경우: 벽, 공기청정기가 있는경우 
                    if((0<=j + dx[d]<C) and (0<=i+dy[d]<R) and (air_map[i + dy[d]][j+dx[d]] != -1)):
                        count+=1 
                        direction.append(d)
                        
                plus = air_map[i][j]//5
                minus = -(air_map[i][j]//5)*count 

                for d in direction:
                    plus_list[i+dy[d]][j+dx[d]] += plus 
                minus_list[i][j] += minus 
    
    for i in range(R):
        for j in range(C):
            air_map[i][j] = air_map[i][j] + plus_list[i][j] + minus_list[i][j]
    
    return air_map

# 2. 공기청정기 바람 
def cleaner(air_map):
    upper = air[0]
    lower = air[1]

    temp_air_map = deepcopy(air_map)

    for i in range(R):
        for j in range(C):
            if(i==0 or i == (R-1)):
                temp_air_map[i][j] = 0
            if(j==0 or j == (C-1)):
                temp_air_map[i][j] = 0
            if(i == air[0][0]):
                temp_air_map[i][j] = 0
            if(i == air[1][0]):
                temp_air_map[i][j] = 0
    temp_air_map[air[0][0]][air[0][1]] = -1 
    temp_air_map[air[1][0]][air[1][1]] = -1 
    
    # 시작점
    upper_now = [air[0][0],air[0][1] +1]
    lower_now = [air[1][0],air[1][1] +1]

    dx = [1,0,-1,0]
    dy_up = [0,-1,0,1]
    dy_low = [0,1,0,-1]
    value = 0
    for i in range(3):
        end = False 
        while(not end):
            if((0<=upper_now[0] + dy_up[i] <R) and (0<= upper_now[1] + dx[i] <C)):
                value = air_map[upper_now[0]][upper_now[1]] 
                temp_air_map[upper_now[0]+dy_up[i]][upper_now[1]+dx[i]] = value 
                upper_now = [upper_now[0] +dy_up[i],upper_now[1]+dx[i]]
            else:
                end = True 
                value = air_map[upper_now[0]][upper_now[1]] 
                temp_air_map[upper_now[0] + dy_up[i+1]][upper_now[1]+dx[i+1]] = value 
                upper_now = [upper_now[0] +dy_up[i+1],upper_now[1]+dx[i+1]]
    
    end = False
    while(not end):
        if(air_map[upper_now[0] + dy_up[3]][upper_now[1]+dx[3]] == -1):
            end = True 
        else:
            value = air_map[upper_now[0]][upper_now[1]] 
            temp_air_map[upper_now[0]+dy_up[3]][upper_now[1]+dx[3]] = value 
            upper_now = [upper_now[0] +dy_up[3],upper_now[1]+dx[3]]

    end = False 
    for i in range(3):
        end = False 
        while(not end):
            if((0<=lower_now[0] + dy_low[i] <R) and (0<= lower_now[1] + dx[i] <C)):
                value = air_map[lower_now[0]][lower_now[1]] 
                temp_air_map[lower_now[0]+dy_low[i]][lower_now[1]+dx[i]] = value 
                lower_now = [lower_now[0] +dy_low[i],lower_now[1]+dx[i]]
            else:
                end = True 
                value = air_map[lower_now[0]][lower_now[1]] 
                temp_air_map[lower_now[0] + dy_low[i+1]][lower_now[1]+dx[i+1]] = value 
                lower_now = [lower_now[0] +dy_low[i+1],lower_now[1]+dx[i+1]]
    
    end = False
    while(not end):

        if(air_map[lower_now[0] + dy_low[3]][lower_now[1]+dx[3]] == -1):
            end = True 
        else:
            value = air_map[lower_now[0]][lower_now[1]] 
            temp_air_map[lower_now[0]+dy_low[3]][lower_now[1]+dx[3]] = value 
            lower_now = [lower_now[0] +dy_low[3],lower_now[1]+dx[3]]

    return temp_air_map 

for t in range(T):
    air_map = spread(air_map)
    air_map = cleaner(air_map)

result = 0
for air in air_map:
    result+=sum(air)

print(result+2)
    




