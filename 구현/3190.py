# 3190 뱀 
N = int(input())
K = int(input())
apples = []

def minus(x):
    return x-1 
for i in range(K):
    apple = list(map(int,input().split()))
    apple = list(map(minus,apple))
    apples.append(apple)

L = int(input())
switch_info = []
for i in range(L):
    switch_info.append(list(input().split()))


def bite(bam):
    # 자기자신
    temp_bam = list(map(tuple,bam))
    temp_bam = set(temp_bam)
    if(len(temp_bam) != len(bam)):
        return True 
    return False

# 뱀이 이동하기 
def move(direction,bam):
    y= bam[len(bam)-1][0]
    x = bam[len(bam)-1][1]

    # 늘리기
    if(direction == [0,1]):
        bam.append([y,x+1])
    elif(direction == [0,-1]):
        bam.append([y,x-1])
    elif(direction == [1,0]):
        bam.append([y+1,x])
    elif(direction == [-1,0]):
        bam.append([y-1,x])
    
    if(bite(bam) == True):
        return True 

    # 사과 먹기 
    is_apple = False 
    index = 0 
    for i in range(len(apples)):
        if([apples[i][0],apples[i][1]] in bam):
            is_apple = True 
            index = i
            break 

    if(is_apple == True):
        apples.remove(apples[index])

    else:
        # 이전거 삭제해주기 
        bam.pop(0)
    
    return bam 

# 뱀 벽 죽음 
def death(bam):
    # 벽 
    for position in bam:
        if(position[0]<0 or position[0]>=N):
            return True 
        elif(position[1]<0 or position[1]>=N):
            return True 
    return False

# 뱀 방향
def where(sec,direct): 
    for info in switch_info:
        if(info[0] == str(sec)):
            if(info[1] == "L"):
                direct = [-(direct[1]),direct[0]]
            elif(info[1] == "D"):
                direct = [direct[1],-(direct[0])]
    return direct 



# 게임 
die = False
my_die = False 
sec = 1
bam = [[0,0]]
direct = [0,1]
while(die != True and my_die != True):
    # 이동
    my_die = move(direct,bam)
    # 죽음 여부
    die = death(bam)
    # 방향
    direct = where(sec,direct)
    sec+=1 
print(sec-1)