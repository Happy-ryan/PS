# def solution(s):
#     total_cnt, zero_cnt = 0, 0
#     answer = []
#     p = len(s)
#     while p != 1:
#         zero_cnt += s.count('0')
#         total_cnt += 1
#         s = '1'*(p - s.count('0'))
#         p = bin(len(s))[2:]
#     print(total_cnt, zero_cnt)
#     return answer
def solution(s):
    total_cnt, zero_cnt = 0, 0
    while len(s) != 1:
        zero_cnt += s.count('0')
        total_cnt += 1
        s = bin(len('1'*(len(s) - s.count('0'))))[2:]
    return [total_cnt, zero_cnt]