# 14503 로봇청소기 
N,M = map(int,input().split()) 
now = list(map(int,input().split())) 
room = []
for i in range(N):
    room.append(list(map(int,input().split()))) 

# 움직이는 가 여부 
moving = True 
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def cleaning(room,now):
    # 청소안된 경우 
    if(room[now[0]][now[1]] == 0):
        room[now[0]][now[1]] = 2 
        return True
    
    # 청소된 경우 
    else:
        return False 

def finding(room,now):
    is_blank = False 
    for i in range(4):
        if(0<=now[0] + dy[i] <N and 0<=now[1] + dx[i] <= M and room[now[0]+dy[i]][now[1]+dx[i]] == 0):
            is_blank = True

    return is_blank
    

# 작동 시작 후 작동을 멈출때까지 청소하는 칸의 개수 
while(moving):
    # 현재칸 청소하기 
    if(cleaning(room,now) == True):
        continue 

    # 이미 청소된 경우 
    else:
        # 빈칸 없는 경우 
        if(finding(room,now) == False):
            # 후진했을때 벽이 있는 경우 
            if(room[now[0] + -(dy[now[2]])][now[1] + -(dx[now[2]])] == 1):
                moving = False 
            # 후진 가능 
            else:
                now[0] = now[0] + -(dy[now[2]])
                now[1] = now[1] + -(dx[now[2]])
        
        # 빈칸있는 경우 
        else:
            to_move = True 
            while(to_move):
                # 반시계 방향 회전      
                now[2] = now[2]-1 
                if(now[2]<0):
                    now[2] = 3 

                # 앞 방향이 청소 안한칸인 경우
                if(room[now[0] + (dy[now[2]])][now[1] + (dx[now[2]])] == 0):
                    now[0] = now[0] + (dy[now[2]])
                    now[1] = now[1] + (dx[now[2]])
                    to_move = False 

clean_area = 0
for i in range(N):
    for j in range(M):
        if(room[i][j] == 2):
            clean_area+=1
print(clean_area)