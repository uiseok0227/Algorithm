# 13458 시험감독 
# 총감독관이 꼭 있어야한다는 생각을 못했음 

N = int(input())
test_class = list(map(int,input().split()))
B,C = map(int,input().split())


# 총감독관 있는 경우 
def with_one(a,b,test):
    result = 1 
    if(test-a<0):
         return result 
    
    result += ((test-a)//b)
    if((test-a)%b != 0):
         result += 1 
    return result 

# # 총감독관이 없는 경우 
# def without_one(b,test):
#     result = 0
#     result += (test//b)
#     if(test%b != 0):
#          result += 1 
#     return result 
     

answer = 0
for test in test_class:
     answer += with_one(B,C,test)
print(answer)