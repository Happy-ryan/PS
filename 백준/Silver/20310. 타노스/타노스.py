def solution(s):
    # 순서 유지한 상태로..
    # 삭제를 시켰을 때 사전순으로 빠르게..
    # 사전순...0은 최대한 앞으로,,1은 최대한 뒤로 가야해..
    # 띠라서 0은 뒤에서 부터 지워 / 1은 앞에서부터 지워
    
    
    zero_cnt, one_cnt = s.count('0') // 2, s.count('1') // 2
    
    zero_idx = []
    one_idx = []
    for idx, i in enumerate(s):
        if i == '0':
            zero_idx.append(idx)
        else:
            one_idx.append(idx)
            
    # print("zero:", zero_idx)
    # print("one:", one_idx)
    
    zero_idx = zero_idx[-zero_cnt:]
    one_idx = one_idx[:one_cnt]
    
    # print("zero:", zero_idx)
    # print("one:", one_idx)
    
    s = list(s)
    for z_idx in zero_idx:
        s[z_idx] = ''
    for o_idx in one_idx:
        s[o_idx] = ''
        
    return ''.join(s)
    
s = input()
print(solution(s))