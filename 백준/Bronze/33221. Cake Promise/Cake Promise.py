t, p = map(int, input().split())

def get_score(row):
    solved = 0
    total_time = 0
    for x in row:
        if x != 'X':
            solved += 1
            total_time += int(x)
    return solved, total_time

# 교수 점수
prof = input().split()
prof_solved, prof_time = get_score(prof)

answer = 0

for _ in range(t - 1):
    row = input().split()
    s, time = get_score(row)
    
    if s > prof_solved:
        answer += 1
    elif s == prof_solved and time <= prof_time:
        answer += 1

print(answer)