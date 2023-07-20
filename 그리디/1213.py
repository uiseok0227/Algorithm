# 1213 팰린드롬 만들기 
import sys 
from copy import deepcopy

word = sys.stdin.readline().strip()
# 1. 아이디어
# 가장 많은 단어 순서대로 정렬후에 리스트에 넣으면 될것 같아
# 케이스를 나누는게 좋을 지..? 너무 케이스가 많음.
word_dict = dict()
word_count_dict = dict()
num = 0
word_list = [0]*50
words = list(word)
words.sort()

# 단어마다 숫자 부여하기
for w in words:
    if(w in word_dict.keys()):
        continue 
    else:
        word_dict[w] = num 
        word_count_dict[num] = w
        num+=1 

# 단어마다 개수 추가해주기
for w in list(word):
    word_list[word_dict[w]] +=1

# 0 없애기
word_list = [x for x in word_list if x != 0]
original_list = deepcopy(word_list)

for i in range(len(word_list)):
    if(word_list[i] % 2 ==0):
        word_list[i] = word_list[i]//2
    else:
        word_list[i] = word_list[i]//2 + 1 

word_length = 0
if(len(word) %2 == 0):
    word_length = len(word)//2
else:
    word_length = len(word)//2+1 

if(sum(word_list) != word_length):
    print("I'm Sorry Hansoo")
else:
    result = ""
    # 길이가 짝수인 경우,
    if(len(word) % 2 ==0):
        for i in range(len(word_list)):
            result += word_count_dict[i]*word_list[i]
        result += result[::-1]
        print(result)

    # 길이가 홀수인 경우
    else:
        center = ""
        for i in range(len(original_list)):
            if(original_list[i]%2 != 0):
                center = word_count_dict[i]
        word_list[word_dict[center]]-=1 
        for i in range(len(word_list)):
            result += word_count_dict[i]*word_list[i]
        result += center +result[::-1]
        print(result)