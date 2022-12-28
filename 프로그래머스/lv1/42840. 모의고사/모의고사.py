def solution(answers):
    answer = []
    check1 = [1, 2, 3, 4, 5] *2000
    check2 = [2, 1, 2, 3, 2, 4, 2, 5] *1250
    check3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(0, len(answers)):
        if check1[i] == answers[i]:
            cnt1 += 1
        if check2[i] == answers[i]:
            cnt2 += 1
        if check3[i] == answers[i]:
            cnt3 += 1
            
    cnt_list = [cnt1, cnt2, cnt3]
    max_cnt = max(cnt_list)
    
    for i, cnt in enumerate(cnt_list):
        if max_cnt == cnt:
            answer.append(i+1)
            
    return answer