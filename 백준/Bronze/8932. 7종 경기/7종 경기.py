from math import floor

t = int(input())

def solution(case):
    
    const = [
        [9.23076, 26.7, 1.835],
        [1.84523, 75, 1.348],
        [56.0211, 1.5, 1.05],
        [4.99087, 42.5, 1.81],
        [0.188807, 210, 1.41],
        [15.9803, 3.8, 1.04],
        [0.11193, 254, 1.88]
        ]
    
    score = 0
    
    for i in range(7):
        A, B, C = const[i]
        score += floor(A * abs(B - case[i]) ** C)
        
    return score

for _ in range(t):
    case = list(map(int, input().split()))
    print(solution(case))