t = int(input())

def solution(cmd, row):
    dic = dict()
    for i in range(26):
        dic[chr(i + 65)] = i + 1
    
    answer = ''
    if cmd == 'C':
        for s in row:
            answer += str(dic[s]) + " "
    else:
        for s in row:
            answer += chr(int(s) + 64) + " "
            
    return answer

for _ in range(t):
    m, cmd = input().split()
    row = list(input().split())
    print(solution(cmd, row))