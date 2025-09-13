l, r = map(int, input().split())

def solution(l, r):
    
    def digit(num: int):
        res = set()
        cnt = 0
        while num:
            x = num % 10
            res.add(x)
            cnt += 1
            num //= 10
        
        if len(res) == cnt:
            return True
        
        return False
        
    
    answer = -1
    for x in range(l, r + 1):
        if digit(x):
            answer = x
            return answer
        
    return answer
    

print(solution(l, r))