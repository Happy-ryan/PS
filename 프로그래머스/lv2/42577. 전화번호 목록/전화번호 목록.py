from collections import Counter

def solution(phone_book):
    answer = True
    prefix_dict = Counter()
    for row in phone_book:
        for i in range(len(row)):
            prefix_dict[row[0: len(row) - i]] += 1
            
    for qs in phone_book:
        if prefix_dict[qs] > 1:
            return False
    return answer