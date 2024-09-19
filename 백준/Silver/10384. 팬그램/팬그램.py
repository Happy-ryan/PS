t = int(input())

def solution(s: str):
    alpabets = 'abcdefghijklmnopqrtuvswxyz'
    inf = int(1e18)
    
    dic = {}
    for x in alpabets:
        dic[x] = 0
    for x in s:
        if x in alpabets:
            dic[x] += 1
    
    sum_val = 0
    check = inf 
    for value in dic.values():
        if value == 0:
            return 'Not a pangram'
        sum_val += value
        check = min(check, value)

    if check >= 3:
        return 'Triple pangram!!!'
    
    if check == 2:
        return 'Double pangram!!'
    
    if check == 1:
        return 'Pangram!'
    
for i in range(t):
    s = input().lower()
    print(f'Case {i + 1}: {solution(s)}')