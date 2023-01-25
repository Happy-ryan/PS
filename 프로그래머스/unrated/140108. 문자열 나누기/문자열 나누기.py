def solution(s):
    answer = 0
    flag = True
    for x in s:
        if flag: # 시작이다!
            cnt = [0, 0]
            cnt[0] += 1
            start = x
            flag = False
        else: # 시작아니다!
            if x == start:
                cnt[0] += 1
            else:
                cnt[1] += 1
        
            if cnt[0] == cnt[1]: # 종료해라
                answer += 1
                flag = True
    if not flag:
        answer += 1
                
    return answer

