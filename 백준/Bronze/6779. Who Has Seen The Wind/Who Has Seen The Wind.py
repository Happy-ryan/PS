h = int(input())
M = int(input())

def solution(h, M):
    t = 1

    while t <= M :
        
        A = ((-6) * (t ** 4)) + (h * (t ** 3)) + (2 * (t ** 2)) + t
        
        if A <= 0 :
            return f"The balloon first touches ground at hour: {t}"
        t += 1
        
    return "The balloon does not touch ground in the given time."

print(solution(h, M))