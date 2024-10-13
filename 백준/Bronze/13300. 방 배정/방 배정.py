n, k = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(n)]

from collections import Counter
from math import ceil

def solution(n, k, students):
    dic = Counter()
    for year in range(1, 7):
        for gender in range(2):
            room_name = year * 10 + gender
            dic[room_name] = 0
    
    for year, gender in students:
        room_name = year * 10 + gender
        dic[room_name] += 1
        
    room_cnt = 0
    for value in dic.values():
        room_cnt += ceil(value / k)
        
    return room_cnt

print(solution(n, k, students))