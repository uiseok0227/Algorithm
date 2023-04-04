# 14500 테크로미노 

N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))


# 가로 3 
def three_garo(y,x):
    result = 0 
    results = [0]

    if(x+2<M):
        # 3개 더해줌 
        result = board[y][x] + board[y][x+1] + board[y][x+2]
    else:
        return 0
    
    if(y-1>=0):
        for i in range(3):
            results.append(result+board[y-1][x+i])
    if(y+1<N):
        for i in range(3):
            results.append(result+board[y+1][x+i])
    if(x+3<M):
        results.append(result+board[y][x+3])
    
    return max(results)

# 세로 3 
def three_sero(y,x):
    result = 0 
    results = [0]

    if(y+2<N):
        # 3개 더해줌 
        result = board[y][x] + board[y+1][x] + board[y+2][x]
    else:
        return 0 
    
    if(x-1>=0):
        for i in range(3):
            results.append(result+board[y+i][x-1])
    if(x+1<M):
        for i in range(3):
            results.append(result+board[y+i][x+1])
    if(y+3<N):
        results.append(result+board[y+3][x])
    
    return max(results)

# 가로 2 
def two_garo(y,x):
    result = 0

    if(x+1<M):
        result = board[y][x] + board[y][x+1]
    else:
        return 0 

    add = []
    if(y-1>=0):
        add.append(board[y-1][x])
        add.append(board[y-1][x+1])
    if(y+1<N):
        add.append(board[y+1][x])
        add.append(board[y+1][x+1])
    
    if(len(add) == 0):
        return 0 
    else:
        add.sort(reverse=True)
        return result+add[0]+add[1]

# 세로 2 
def two_sero(y,x):
    result = 0

    if(y+1<N):
        result = board[y][x] + board[y+1][x]
    else:
        return 0 

    add = []
    if(x-1>=0):
        add.append(board[y][x-1])
        add.append(board[y+1][x-1])
    if(x+1<M):
        add.append(board[y][x+1])
        add.append(board[y+1][x+1])
    
    if(len(add) == 0):
        return 0 
    else:
        add.sort(reverse=True)
        return result+add[0]+add[1]

    

answer = 0
for i in range(N):
    for j in range(M):
        answer = max(answer,three_garo(i,j)) 
        answer = max(answer,three_sero(i,j))
        answer = max(answer,two_garo(i,j))
        answer = max(answer,two_sero(i,j))
print(answer)   