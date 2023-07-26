# 백트래킹. 소비전력이 더 적은게 나타나면 그 방향으로
# 킨 경우) 끄기 / 범위 내일때 멈춰두기 / 바꾸기 

import sys 
sys.setrecursionlimit(10 ** 6)

# 희망온도 판단 
def want_temp(now_temp):
    global temp,lower,upper
    if(abs(now_temp - lower) > abs(now_temp-upper)):
        return lower
    else:
        return upper 

# 확인 
def check(now_answer,now_temp,now_board,onboard,t1,t2):
    global answer,end 
    if(now_answer>=answer):
        return False 
    
    if(onboard[now_board] == 1):
        if(now_temp<t1 or now_temp>t2):
            return False
    
    if(now_board == len(onboard)-1):
        if(now_answer < answer):
            answer = now_answer 
        return False 
    
    return True 

def backtrack(now_temp,onboard,now_board,now_answer,how):
    global answer,temp,lower,upper,elec_same,elec_diff
    
    # 끄기 
    if(how==0):
        if((temp - now_temp) > 0):
            now_temp+=1 
        elif(temp == now_temp):
            now_temp = temp 
        else:
            now_temp -= 1  
        
    # 범위 내일때 멈춰두기 
    elif(how == 1):
        if(now_temp>= lower and now_temp<=upper):
            now_answer += elec_same
        else:
            return 0 
            
    # 바꾸기 
    elif(how == 2):
        wanting_temp = want_temp(now_temp)
        if(wanting_temp - now_temp>0):
            now_temp +=1 
            now_answer += elec_diff 
        else:
            now_temp -= 1 
            now_answer += elec_diff 
    
    now_board+=1 
    # print("now_board: ",now_board," now_temp: ",now_temp," now_answer: ",now_answer," how: ",how)
    # 확인 
    if(check(now_answer,now_temp,now_board,onboard,lower,upper) == False):
        return 0
    for i in range(3):
        backtrack(now_temp,onboard,now_board,now_answer,i)

                
            
    
def solution(temperature, t1, t2, a, b, onboard):
    global answer,temp,lower,upper,elec_same,elec_diff,end
    answer,temp,lower,upper,elec_diff,elec_same,end = 1000000,temperature,t1,t2,a,b,len(onboard)

    now_answer = 0 
    now_temp = temperature
    now_board = 0 
        
    for i in range(3):
        now_answer = 0
        backtrack(now_temp,onboard,now_board,now_answer,i)
    
    return answer

print(solution(28,18,26,10,8,[0, 0, 1, 1, 1, 1, 1]))
