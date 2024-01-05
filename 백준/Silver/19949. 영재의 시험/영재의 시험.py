# https://www.acmicpc.net/problem/19949

right_numbers = list(map(int, input().split()))

problem_number = 10
ans = []
cnt = 0
def dfs(level):
    global cnt
    if level == problem_number:
        if check() and score_calculate() >= 5:
            # print(ans, score_calculate())
            cnt += 1
        return
    for i in range(1, 6):
        ans.append(i)
        dfs(level + 1)
        ans.pop()
        
def check():
    # 초기값
    # cnt = 1인 이유: s를 선택함 
    cnt = 1
    s = ans[0]
    for num in ans[1:]:
        # 같으면 +1
        if s == num:
            cnt += 1
        else:
            # 같지 않으면 1로 초기화: 1인 이유: num이 s로 선택됨.
            cnt = 1
            s = num
        if cnt == 3:
            return False
    return True
        
def score_calculate():
    score = 0
    for number, right in zip(ans, right_numbers):
        if number == right:
            score += 1
    return score

dfs(0)
print(cnt)