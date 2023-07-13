# 15684 사다리 조작 
from itertools import combinations
from copy import deepcopy

N,M,H = map(int,input().split())

ladder_map = [[0 for _ in range(2*N - 1)] for _ in range(H+2)]
# 홀수 줄은 1로 만들기 
for i in range(2*N-1):
    if(i%2 != 0):
        continue
    for j in range(H+2): 
        ladder_map[j][i] = 1 

# 사다리 연결시켜주기 
for i in range(M):
    a,b = map(int,input().split())
    ladder_map[a][2*b-1] = 1 

# 0인부분 찾아주기 
empty_list = []
for i in range(1,H+1):
    for j in range(0,2*N-1):
        if(j%2 != 0):
            if(ladder_map[i][j] == 0):
                empty_list.append([i,j])


def check(start,ladder_map):
    now = [0,start]
    end = False 
    while(not end):
        # 오른쪽 쭉가기 
        moved = False 
        stop = False 
        while(not stop):
            if(now[1] +1 <2*N-1 and ladder_map[now[0]][now[1]+1] == 1):
                now = [now[0],now[1]+1]
                moved = True        
            else:
                stop = True 

        # 오른쪽 움직이지 않은 경우만 왼쪽 살피기 
        if(moved == False):
            stop = False 
            while(not stop):
                if(now[1]-1>=0 and ladder_map[now[0]][now[1]-1] == 1):
                    now = [now[0],now[1]-1]
                    moved = True 
                else:
                    stop = True 
        # 밑으로 내려가기 
        now = [now[0]+1,now[1]]
        if(now[0] == H+1):
            if(now[1] == start):
                return True 
            else :
                return False 

result = True 
# 사다리 0개 추가로 가능한지 확인하기 
for i in range(2*N-1):
    if(i%2==0):
        if(check(i,ladder_map) == False):
            result = False 
if(result == True):
    print(0)
    exit(0)

# 사다리 1개 추가로 가능한지 확인하기 
comb_1 = combinations(empty_list,1)
for c in comb_1:
    result = True 
    test_ladder_map = deepcopy(ladder_map)
    test_ladder_map[c[0][0]][c[0][1]] = 1 
    for i in range(2*N-1):
        if(i%2==0):
            if(check(i,test_ladder_map) == False):
                result = False 
    if(result == True):
        print(1)
        exit(0)

# 사다리 2개 추가로 가능한지 확인하기
comb_2 = combinations(empty_list,2)
for comb in comb_2:
    result = True 
    test_ladder_map = deepcopy(ladder_map)
    for c in comb:
        test_ladder_map[c[0]][c[1]] = 1 

    for i in range(2*N-1):
        if(i%2==0):
            if(check(i,test_ladder_map) == False):
                result = False 
    if(result == True):
        print(2)
        exit(0)

# 사다리 3개 추가로 가능한지 확인하기 
comb_3 = combinations(empty_list,3)
for comb in comb_3:
    result = True 
    test_ladder_map = deepcopy(ladder_map)
    for c in comb:
        test_ladder_map[c[0]][c[1]] = 1 
        
    for i in range(2*N-1):
        if(i%2==0):
            if(check(i,test_ladder_map) == False):
                result = False 
    if(result == True):
        print(3)
        exit(0)

if(result == False):
    print(-1)


