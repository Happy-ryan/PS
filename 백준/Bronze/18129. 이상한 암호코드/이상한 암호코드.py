S, K = input().split()

def solution(S, K):
    
    K = int(K)
    S = S.upper()
    
    def custom_split(s):
        tmp = []
        
        
        for x in s:
            if not tmp:
                tmp.append(x)
            else:
                if tmp[-1] == x:
                    tmp.append(x)
                else:
                    tmp.append('/')
                    tmp.append(x)
                    
        tmp = ''.join(tmp).split('/')
        
        
        return tmp
    
    ans = ''
    tmp = custom_split(S)
    # print(tmp)
    check = set()
    for t in tmp:
        if t[0] in check:
            continue

        if len(t) >= K:
            ans += '1'
        else:
            ans += '0'
        
        check.add(t[0])
            
    return ans
    
    
print(solution(S, K))