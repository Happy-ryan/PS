s = input()

def solution(s):

    for i in range(len(s) - 1, -1, -1):
        if s[i] != s[len(s) - i - 1]:
            return 'boop'
    return 'beep'

print(solution(s))