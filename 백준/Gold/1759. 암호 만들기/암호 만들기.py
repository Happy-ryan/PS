l, c = map(int, input().split())
alpabets = list(input().split())

def solution(l, c, alpabets):
    # 최소 1개의 모음 / 최소 2개의 자음
    # 정렬된 암호
    alpabets.sort()
    
    ans = []
    def cal(ans):
        sum_1, sum_2 = 0, 0
        for x in ans:
            if x in 'aeiou':
                sum_1 += 1
            else:
                sum_2 += 1
        if sum_1 >= 1 and sum_2 >= 2:
            return True
        return False
    
    # print(alpabets)
    def back(l, c, idx):
        if len(ans) == l:
            if cal(ans):
                print(''.join(ans))
            return
        # idx를 선택했을 때
        if idx < c:
            ans.append(alpabets[idx])
            # print("*: ", ans)
            back(l, c, idx + 1)
            ans.pop()
            # idx를 선택하지 않았을 때
            back(l, c, idx + 1)
            
            # print("**: ",ans)
        
    back(l, c, 0)
    
solution(l, c, alpabets)