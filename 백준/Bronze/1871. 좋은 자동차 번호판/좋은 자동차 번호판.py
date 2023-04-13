# https://www.acmicpc.net/problem/1871

def solution(s):
    first, second = s.split("-")
    
    sum_val = 0
    n = len(first)
    for idx, x in enumerate(first):
        i = n - idx - 1
        sum_val += (ord(x) - 65) * (26 ** i)
    
    if abs(sum_val - int(second)) <= 100:
        return "nice"
    else:
        return "not nice"
        
t = int(input())
for _ in range(t):
    print(solution(input()))