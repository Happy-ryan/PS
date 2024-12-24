# 남학생 - 스위치 번호가 자기가 받은 수의 배수이면 그 스위치 상태 바꾼다.
# 여학생 - 자기가 받은 수와 같은 스위치 중심으로 좌우가 대칭이면 가장 많은 스위치를 포함하는 그 구간에 속한 스위치 상태 전부 변경 /  스위치 개수는 항상 홀수

n = int(input())
switchs = ['*'] + list(map(int, input().split()))
t = int(input())
cmds = [list(map(int, input().split())) for _ in range(t)]

def solution(switchs, cmds):
    
    def man(num):
        for x in range(num, n + 1, num):
            switchs[x] ^= 1
    
    def woman(num):
        flag = True
        max_val = 0
        for val in range(1, n // 2 + 1):
            l = num - val
            r = num + val
            if l < r and 0 < l and r < n + 1 and switchs[l] == switchs[r]:
                max_val = val
            else:
                max_val = val - 1
                break
            # print(f"val: {val} / l: {l}, r : {r} / s_l :{switchs[l]} / s_r : {switchs[r]}")
            
        min_l = num - max_val
        max_r = num + max_val
        # print(f"val: {max_val}, l: {min_l}, r: {max_r}")
        for x in range(min_l, max_r + 1):
            switchs[x] ^= 1
            
            
    for cmd in cmds:
        gender, num = cmd
        if gender == 1:
            man(num)
        else:
            woman(num)
        # print(f"성벌 : {gender}, 상태: {switchs}")
    
    return switchs[1:]
        
ans = solution(switchs, cmds)
for i in range(0, len(ans), 20):
    print(*ans[i:i+20])
