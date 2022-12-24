def solution(s):
    s = s.lower()
    print(s)
    p_cnt, y_cnt = 0, 0
    for x in s:
        if x == 'p':
            p_cnt += 1
        elif x == 'y':
            y_cnt += 1
    if p_cnt == y_cnt:
        return True
    else:
        return False
