t = int(input())

def solution(num: int):
    
    def make_min_num(x: int):
        if len(str(x)) < 4:
            x *= 10 * (4 - len(str(x)))
            
        digit = []
        while x:
            d = x % 10
            x //= 10
            digit.append(d)
        
        # 최솟값
        digit.sort()
        # min_num = digit[0] * 1000 + digit[1] * 100 + digit[2] * 10 + digit[3] * 1
        min_num = str(digit[0]) + str(digit[1]) + str(digit[2]) + str(digit[3])
        # 최대값
        digit.sort(reverse=True)
        # max_num = digit[0] * 1000 + digit[1] * 100 + digit[2] * 10 + digit[3] * 1
        max_num = str(digit[0]) + str(digit[1]) + str(digit[2]) + str(digit[3])
        
        return (min_num, max_num)
    

    cnt = 0
    while num != 6174:
        min_num, max_num = make_min_num(num)
        num = int(max_num) - int(min_num)
        # print(f"num: {num}")
        cnt += 1
    
    return cnt

for _ in range(t):
    x = int(input())
    print(solution(x))