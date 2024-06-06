n = int(input())
lifes = [input() for _ in range(n)]

def solution(lifes):
    
    def cal_score(life: str):
        score = 0
        for x in life:
            if x != ' ':
                score += ord(x) - 64
        return score
    
    for life in lifes:
        score = cal_score(life)
        if score == 100:
            print('PERFECT LIFE')
        else:
            print(score)
            

solution(lifes)