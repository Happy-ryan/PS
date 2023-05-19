# https://www.acmicpc.net/problem/14920

def solution(num: int, level:int):
    if num == 1:
        return level
    if num % 2 == 0:
        x = num//2
    else:
        x = 3 * num + 1
        
    return solution(x, level + 1)

n = int(input())
print(solution(n, 1))