# 15686 치킨 배달 
from itertools import combinations

N,M = map(int,input().split())
city_map = []
for i in range(N):
    city_map.append(list(map(int,input().split())))

# 치킨집 위치 파악
chickens = []
houses = []
for i in range(N):
    for j in range(N):
        if(city_map[i][j] == 2):
            chickens.append([i,j])
        if(city_map[i][j] == 1):
            houses.append([i,j])

# M개의 치킨집 선택
chicken_lists = combinations(chickens,M)

answers = []
for chicken_list in chicken_lists:
    result = 0
    for house in houses:
        distance = 1000000000000000
        for chicken in chicken_list:
            distance = min(distance,(abs(chicken[0]-house[0])+abs(chicken[1]-house[1])))
        result+=distance
    answers.append(result)

print(min(answers)) 

