# 14499 주사위 굴리기 
# y,x 를 헷갈렸다. 항상 일반적이라고 생각말고 문제를 집중해서 읽자.
import sys 

N,M,y,x,K = map(int,input().split())
board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
order = list(map(int,input().split()))

# 이동 
def move(dice,k,now):
    temp = dice[0]
    y = now[0]
    x = now[1]
    # 동 
    if(k==1):
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = temp 
        x = x+1 
    # 서 
    elif(k==2):
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = temp 
        x = x-1 
    # 북 
    elif(k==3):
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = temp 
        y = y-1 
    # 남 
    else:
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = temp 
        y = y+1 
    return [y,x]

# 명령 무시 
def out_order(k,now):
    y = now[0]
    x = now[1]

    # 동
    if(k==1):
        if(x+1<0 or x+1>=M):
            return True 
    # 서
    elif(k==2):
        if(x-1<0 or x-1>=M):
            return True 
    # 북 
    elif(k==3):
        if(y-1<0 or y-1>=N):
            return True 
    # 남 
    else:
        if(y+1<0 or y+1>=N):
            return True 
    return False 

# 주사위 
dice = [0,0,0,0,0,0]

# 현재 좌표 
now = [y,x]
for k in order:
    if(out_order(k,now) == True):
        continue 
    now = move(dice,k,now)
    if(board[now[0]][now[1]] == 0):
        board[now[0]][now[1]] = dice[5]
    else:
        dice[5] = board[now[0]][now[1]]
        board[now[0]][now[1]] = 0 
    print(dice[0])