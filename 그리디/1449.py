# 수리공 항승 

import sys 

N,L = map(int,sys.stdin.readline().split())
water_map = list(map(int,sys.stdin.readline().split()))
water_map.sort()
# 아이디어
# 1. 물이 새는 곳의 위치를 정렬 후에 차이계산 
# N,L <= 1000 

# diff_list = []
# sum = 0 
# for i in range(1,len(water_map)):
#     diff = water_map[i] - water_map[i-1]
#     if(diff<=L-1):
#         if(sum+diff<L-1):
#             if(i==len(water_map)-1):
#                 diff_list.append(diff)
#             sum+=diff 
#         elif(sum+diff == L-1):
#             sum+=1 
#             diff_list.append(sum)
#             sum = 0
#         else:
#             diff_list.append(sum)
#             sum += diff
#     else:
#         if(sum!=0):
#             diff_list.append(sum)
#         diff_list.append(diff)

# # print(diff_list)

# result = 0 
# is_in = 0
# is_out = 0
# outer = 0

# for i in range(len(diff_list)):
#     diff = diff_list[i]
#     if(diff>L-1):
#         if(i==0 or i==len(diff_list)-1):
#             outer += 1
#         is_out+=1 
#     else:
#         is_in += 1

# if(outer>0):
#     if(is_in ==0):
#         print(is_out+1)
#     else:
#         print(outer+is_in)
# else:
#     if(is_in==0):
#         print(is_out+1)
#     else:
#         print(is_in)


# 아이디어 2 테이프를 순서대로 붙여가면서 
start = water_map[0]
result = 1 
for location in water_map[1:]:
    if(location in range(start,start+L)):
        continue 
    else:
        start = location
        result+=1 
print(result)