# 5430 AC

# R , D 함수 
# R은 배열에 있는 수의 순서 뒤집기 
# D는 첫번째 수 버리기. 배열이 비어있는데 D를 사용 -> 에러 
T = int(input())
for i in range(T):
    p = input() # 함수
    n = int(input()) # 배열에 들어있는 수의 개수 
    array = input().replace("[","").replace("]","")
    if(n == 0 or len(array) == 0):
        array = []
    else:
        array = list(map(int,array.split(",")))
    
    error = False
    direction = "left"
    start = 0
    end = len(array)

    for i in range(len(p)):

        # 왼쪽, 오른쪽 바꿔주기 
        if(p[i] == "R"):
            if(direction == 'left'):
                direction = 'right'

            elif(direction == 'right'):
                direction = 'left'
         
        elif(p[i]=="D"):
            # 에러 
            if(start == end):
                error = True

            # 왼쪽인경우
            if(direction == 'left'):
                start = start+1 
            
            # 오른쪽인 경우 
            if(direction == 'right'):
                end = end-1
            
    if(error == True):
        print("error")

    else:
        array = array[start:end]
        if(direction == 'left'):
            print(str(array).replace(" ",""))
        else:
            array.reverse()
            print(str(array).replace(" ",""))
