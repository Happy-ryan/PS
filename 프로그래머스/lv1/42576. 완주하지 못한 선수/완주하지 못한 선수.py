from collections import Counter
def solution(participant, completion):
    p_dict = Counter(participant)
    c_dict = Counter(completion)
    for key in Counter(participant).keys():
        check = p_dict[key] - c_dict[key]
        if check == 1:
            return key