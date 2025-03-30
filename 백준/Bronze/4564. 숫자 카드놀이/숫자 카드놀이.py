def solution(num):
    
    ans = [num]
    while True:
        if len(num) == 1:
            return ans
        cnt = 1
        for x in num:
            cnt *= int(x)
        num = str(cnt)
        ans.append(num)
        
while True:
    num = input()
    if num == '0':
        break
    print(*solution(num))