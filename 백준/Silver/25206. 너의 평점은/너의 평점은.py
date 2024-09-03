infos = [list(input().split()) for _ in range(20)]

def solution(infos):
    dic = {
        'A+': 4.5,
        'A0': 4.0,
        'B+': 3.5,
        'B0': 3.0,
        'C+': 2.5,
        'C0': 2.0,
        'D+': 1.5,
        'D0': 1.0,
        'F' : 0.0
    }
    total_score = 0
    total_score_and_grade = 0
    for info in infos:
        _, score, grade = info
        score = float(score)
        if grade != 'P':
            total_score += score
            total_score_and_grade += score * dic[grade]
    
    return total_score_and_grade / total_score
            
print(solution(infos))