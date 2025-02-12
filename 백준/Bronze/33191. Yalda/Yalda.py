a = int(input())
w = int(input())
p = int(input())
n = int(input())

def solution(a, w, p, n):
    if a >= w:
        return 'Watermelon'
    elif a >= p:
        return 'Pomegranates'
    elif a >= n:
        return 'Nuts'
    else:
        return 'Nothing'

print(solution(a, w, p, n))