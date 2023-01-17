answer = []

def get_money(emoticons, emoticions_discount, users): 
        global answer
        total, person = 0, 0
        for user_discount, user_standard in users:
            money = 0
            for i in range(len(emoticions_discount)):
                if emoticions_discount[i] >= user_discount:
                    money += emoticons[i] * (100 - emoticions_discount[i]) // 100
            if money >= user_standard:
                person += 1
            else:
                total += money
                
            answer.append((person, total))
            
def solution(users, emoticons):
    # 완전탐색을 위한 수형도 작성 by DFS(백트래킹 할인되는 경우의수, 중복 가능)
    dis = []
    visited = []
    def dfs(lev):
        if lev == len(emoticons):
            a = visited.copy()
            dis.append(a)
            return
        for i in [10, 20, 30, 40]:
            visited.append(i)
            dfs(lev + 1)
            visited.pop()
    dfs(0)
    for emoticons_discount in dis:
        get_money(emoticons, emoticons_discount, users)
    answer.sort()
    
    return list(answer[-1])