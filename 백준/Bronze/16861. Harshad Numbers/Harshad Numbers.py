n  = int(input())

def solution(n):
    
    def harshad(num):
        sum_val = sum(map(int, str(num)))
        return 1 if num % sum_val == 0 else 0
    
    init_num = n
    
    cnt = 0
    while True:
        if harshad(n):
            return init_num + cnt
        n += 1
        cnt += 1
                
print(solution(n))