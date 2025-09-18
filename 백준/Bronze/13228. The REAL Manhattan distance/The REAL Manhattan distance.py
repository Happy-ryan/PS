t = int(input())

def solution(x1, y1, f1, x2, y2, f2):
    
    X = abs(x1 - x2)
    Y = abs(y1 - y2)
    
    return f1 + X + Y + f2


for _ in range(t):  
    x1, y1, f1, x2, y2, f2 = map(int, input().split())
    print(solution(x1, y1, f1, x2, y2, f2))