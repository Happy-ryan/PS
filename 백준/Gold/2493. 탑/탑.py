n = int(input())
tops = list(map(int, input().split()))

def solution(n, tops):
    # 6(0) 9(0) 5(2) 7(2) 4(4)
    # [6] 9 <- 5 .. 6은 의미가 없다. 왜? 9가 6을 가린다!! 6을 필요가 없어짐.
    # 들어올 탑의 왼쪽에 나보다 작은 탑이 존재해서는 안된다!
    stack = []
    memo = [0 for _ in range(n)]
    for idx, top in enumerate(tops):
    
        # 새로운 탑의 높이보다 왼쪽에 작은 탑들은 제외!
        while stack and stack[-1][0] <= top:
            stack.pop()
        
        # 스택이 비어있다면 왼쪽 탑이 없다. 수신하는 탑이 존재하지 않는다.
        if len(stack) == 0:
            memo[idx] = 0
        # 스택이 있다. 왼쪽에 내 신호를 수신하는 탑이 존재하는데
        #   (~~~5의 입장에서는 필요없음) 9 5
        # 9가 5의 레이저 수신
        # stack에서 가장 위에 있는 것이 레이저를 수신한다.
        else:
            memo[idx] = stack[-1][1] + 1
            
        stack.append((top, idx))
        
        
    return memo

print(*solution(n, tops))