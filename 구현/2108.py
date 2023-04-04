# 2108 통계학 

import sys 
N = int(sys.stdin.readline())
num_lists = []
for i in range(N):
    num_lists.append(int(sys.stdin.readline()))

# 산술평균 
print(int(round((sum(num_lists)/N),0)))

# 중앙값 
num_lists.sort()
print(num_lists[N//2])

# 최빈값
if(N==1):
    print(num_lists[0])
else:
    num_dict = dict() 
    for num in num_lists:
        try:
            num_dict[num] += 1
        except:
            num_dict[num] = 1

    sort_list = []
    for k,v in num_dict.items():
        sort_list.append([k,v])

    sort_list.sort(key = lambda x : x[1],reverse=True)
    if(sort_list[0][1] == sort_list[1][1]):
        print(sort_list[1][0])
    else:
        print(sort_list[0][0])

# 범위
max_num = max(num_lists)
min_num = min(num_lists)

# 둘 다 + 
if(max_num>0 and min_num >0):
    print(max_num - min_num)
# 둘 다 -
elif(max_num<0 and min_num<0):
    print(max_num - min_num)
# 둘 중하나 + 
else:
    print(abs(max_num - min_num))
