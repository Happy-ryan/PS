# 조건1 : 선행스킬이 존재한다면 선행스킬을 반드시 배운다,
# 조건2 : 선행스킬이 없다면 순서에 상관 없이 배울 수 있다
# 조건2  해설 : skill-abc//skilltree-z z는 배울 수 있음. 왜냐 스킬트리 안에 선행 스킬이 하나도 있지 않음
def solution(skill, skill_trees):
    answer = 0
    ans = set()
    for i in range(len(skill)):
        ans.add(skill[:i + 1])
    ans.add('')
    
    for skill_tree in skill_trees:
        skill_order = ''
        for i, x in enumerate(skill_tree):
            if x in skill:
                skill_order += x
        print(skill_order)
        
        if len(skill_order) == '':
            answer += 1
        else:
            if skill_order in ans:
                answer += 1
            
    return answer