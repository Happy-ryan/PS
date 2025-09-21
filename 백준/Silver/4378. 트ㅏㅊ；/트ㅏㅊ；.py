import sys

def solution(s):
    
    keyboard = [
        ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'"],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']   
    ]
    
    dic = {}
    for i in range(4):
        row = keyboard[i]
        for j in range(1, len(row)):
            dic[row[j].upper()] = row[j - 1].upper()
    
    answer = ''
    for x in s:
        if x == ' ':
            answer += ' '
        else:
            answer += dic[x]
    return answer


for line in sys.stdin:
    print(solution(line.rstrip("\n")))