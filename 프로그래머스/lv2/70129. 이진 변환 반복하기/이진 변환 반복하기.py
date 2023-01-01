total_cnt, zero_cnt = 0, 0

def solution(s):
    answer = []
    def f(s): 
        global total_cnt
        global zero_cnt 
        res = ''
        if len(s) == 1:
            answer.append(total_cnt)
            answer.append(zero_cnt)
            return
        for x in s:
            if x == '1':
                res += '1'
            else:
                zero_cnt += 1
        p = bin(len(res))[2:]
        total_cnt += 1
        f(p)
    f(s)
    return answer