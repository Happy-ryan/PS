def solution(a, b):
    answer = ''
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    day = 4 # 1월 1일의 요일이 기준
    for i in range(1, a):
        day += month[i] # 1 + 2 + 3 + 4 = 31 + 29 + 31 + 30
    day += b - 1 # 1 ~ 24
    
    return week[day % 7]