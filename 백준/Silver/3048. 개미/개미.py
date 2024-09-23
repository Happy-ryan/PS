n1, n2 = map(int, input().split())
ants1 = list(input())
ants2 = list(input())
t = int(input())

def solution(ants1, ants2, t):
    state = []
    # ants1은 홀수 / ant2는 짝수
    # 내 앞에 있는 개미가 반대방향인지 알려면 ants1소속인지, ants2소속인지 알 필요가 있다.
    # 그 때마다 in 써서 찾을 수도 있는데 중복되는 알파벳이 없으므로 짝수, 홀수로 소속을 대신 파악한다.
    for idx in range(len(ants1) - 1, -1, -1):
        state.append(str(idx * 2 + 1))
    for idx in range(len(ants2)):
        state.append(str(idx * 2))
    
    
    # 홀수는 오른쪽으로만 / 짝수는 왼쪽으로만 이동!! 한 방향 이동이 포인트!
    # 짝을 지을 때 (홀수, 짝수)인 상태만 변경이 발생해야한다!
    # (짝수, 홀수) 상태면 홀수는 왼쪽, 짝수가 오른쪽으로 이동하므로 한 방향으로만 이동하는게 아님!!
    # (move1, move2)로 짝을 만들기 때문에 move1 홀수 / move2 짝수일 때만 변경!
    def move(state):
        move_ants = []
        idx = 0
        while idx < len(state) - 1:
            move1 = int(state[idx]) % 2
            move2 = int(state[idx + 1]) % 2
            if move1 != move2 and (move1 == 1 and move2 == 0):
                move_ants.append((idx, idx + 1))
                idx += 2
            else:
                idx += 1
        
        for x, y in move_ants:
            state[x], state[y] = state[y], state[x]
        
        return state
        
    def change(state):
        ans = ''
        for x in state:
            x = int(x)
            if x % 2 == 1:
                ans += ants1[x // 2]
            else:
                ans += ants2[x // 2]
        return ans
    
    ans = change(state)
    for i in range(t):
        state = move(state)
        ans = change(state)
    return ans
    
print(solution(ants1, ants2, t))