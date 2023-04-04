# 14502 연구소 
from itertools import combinations
from copy import deepcopy

N,M = map(int,input().split())

lab = []
for i in range(N):
    lab.append(list(map(int,input().split())))

# 비어있는 곳 및 바이러스 위치 확인하기 
list_0 = []
list_virus = []
for i in range(N):
    for j in range(M):
        if(lab[i][j] == 0):
            list_0.append([i,j])
        if(lab[i][j] == 2):
            list_virus.append([i,j])

# 바이러스 퍼지기 함수 
def spread(virus,map_lab):
    # 좌 우 상 하 
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        x = virus[1]+dx[i]
        y = virus[0]+dy[i]

        if(x>=0 and x<M and y>=0 and y<N):
            if(map_lab[y][x] == 0):
                map_lab[y][x] = 2 
                spread([y,x],map_lab)


answer = 0
# 비어있는 곳 3개 조합 만들기
for combs in combinations(list_0,3):
    temp_lab = deepcopy(lab)

    for comb in combs:
        temp_lab[comb[0]][comb[1]] = 1
    
    # 바이러스 퍼지기 
    for virus in list_virus:
        spread(virus,temp_lab)

    # 0개수 파악하기 
    result = 0
    for t in temp_lab:
        result+=t.count(0)

    answer = max(result,answer)

print(answer)
    