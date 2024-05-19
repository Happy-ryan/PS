e, f, c = map(int, input().split())

def solution(e, f, c):
    s = e + f
    sum = 0
    
    while True:
        if s < c:
            break
        sum += s // c
        s = s % c + s // c

    return sum

print(solution(e, f, c))