s = list(input())

def solution(s):
    
    if '3' not in s and\
        '4' not in s and\
        '5' not in s and\
        '6' not in s and\
        '7' not in s and\
        '9' not in s:
            if '2' in s and '0' in s and '1' in s and '8' in s:
                if s.count('2') == s.count('0') == s.count('1') == s.count('8'):
                    return 8
                else:
                    return 2
            else:
                return 1
    else:
        return 0
    

print(solution(s))