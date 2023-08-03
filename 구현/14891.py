# 14891 톱니바퀴 

# 4개의 톱니바퀴 차례로 구현 
import sys 
gear_0 = list(map(int,sys.stdin.readline().strip()))
gear_1 = list(map(int,sys.stdin.readline().strip()))
gear_2 = list(map(int,sys.stdin.readline().strip()))
gear_3 = list(map(int,sys.stdin.readline().strip()))
gear = [gear_0,gear_1,gear_2,gear_3]

rotation = int(sys.stdin.readline())
rotate_info = []
for r in range(rotation):
    rotate_info.append(list(map(int,sys.stdin.readline().split())))

# 먼저 돌리고 나서 확인하는게 아니라 초기상태를 확인해야함 

# 돌리기 
def rotate(rotate_gear,where):
    now = gear[rotate_gear]
    # 시계방향 돌리기 
    if(where == 1):
        cache = now[7]
        for i in range(7,0,-1):
            now[i] = now[i-1]
        now[0] = cache
    # 반기계방향 돌리기 
    else:
        cache = now[0]
        for i in range(0,7):
            now[i] = now[i+1]
        now[7] = cache 

for info in rotate_info:
    rotate_gear,where = info[0]-1,info[1]
    # 회전 목록 
    rotation_list = [[rotate_gear,where]]
    
    # 왼쪽 돌리기 
    left = where 
    for i in range(rotate_gear-1,-1,-1):
        if(gear[i][2] == gear[i+1][6]):
            break 
        else:
            left = -left 
            rotation_list.append([i,left])


    # 오른쪽 돌리기 
    right = where 
    for i in range(rotate_gear+1,4):
        if(gear[i][6] == gear[i-1][2]):
            break 
        else:
            right = -right 
            rotation_list.append([i,right])
    
    # 돌리기 
    for r in rotation_list:
        rotate(r[0],r[1])

result = gear[0][0] + 2*gear[1][0] + 4*gear[2][0] + 8*gear[3][0]
print(result)