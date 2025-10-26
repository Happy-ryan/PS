n = int(input())
dominos = [list(map(int, input().split())) for _ in range(n)]

def solution(n, dominos):
    
    dominos.sort(key= lambda x: x[0])
    
    fd, fl = dominos[0]
    
    cnt = 1
    
    for dm in dominos[1:]:
        nd, nl = dm
        if fd + fl < nd:
            cnt += 1
        fd, fl = nd, nl
    
    return cnt
    

print(solution(n, dominos))