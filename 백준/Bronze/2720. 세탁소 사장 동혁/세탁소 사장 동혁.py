t = int(input())

def solution(money):
    nums = [25, 10, 5, 1]
    cnts = [0, 0, 0, 0]
    
    for idx in range(4):
        num = nums[idx]
        
        cnts[idx] += money // num
        money %= num
        
    return cnts

for _ in range(t):
    money = int(input())
    print(*solution(money))