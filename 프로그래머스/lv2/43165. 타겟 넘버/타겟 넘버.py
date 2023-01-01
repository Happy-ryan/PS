total = 0
answer = 0

def dfs(lev, numbers, target):
    global total, answer
    if lev == len(numbers):
        if total == target:
            answer += 1
        return
    x = numbers[lev] 
    # + 인 경우
    total += x
    dfs(lev + 1, numbers, target)
    total -= x
    # - 인 경우
    total -= x
    dfs(lev + 1, numbers, target)
    total += x
    
def solution(numbers, target):
    dfs(0, numbers, target)
    return answer