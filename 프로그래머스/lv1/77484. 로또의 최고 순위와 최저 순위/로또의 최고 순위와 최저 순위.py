from collections import Counter

def rank(x):
    if x == 6:
        return 1
    elif x == 5:
        return 2
    elif x == 4:
        return 3
    elif x == 3:
        return 4
    elif x == 2:
        return 5
    else:
        return 6
    
def solution(lottos, win_nums):
    answer = []
    
    lottos_dict = Counter(lottos)
    win_dict = Counter(win_nums)
    
    same_cnt = 0
    zero_cnt = lottos_dict[0]
    
    for key in lottos_dict.keys(): # key는 max6개 min 1개
        if key in win_dict.keys():
            same_cnt += 1
    
    return [rank(same_cnt + zero_cnt), rank(same_cnt)]