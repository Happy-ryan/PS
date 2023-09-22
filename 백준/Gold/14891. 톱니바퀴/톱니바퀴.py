# https://www.acmicpc.net/problem/14891
# 12시방향의 상태 : 인덱스 0번으로 정의!
ts = ['인덱스맞추기용'] + [input() for _ in range(4)]
k = int(input())
cmds = [list(map(int, input().split())) for _ in range(k)]
# 톱니바퀴의 회전에서 주목해야하는 포인트
# -> 1번의 인덱스 2번 - 2번의 인덱스 6번
# -> 2번의 인덱스 2번 - 3번의 인덱스 6번
# -> 3번의 인덱스 2번 - 4번의 인덱스 6번

# 10101111
# 반시계 회전 0101111
def ccw(t: str):
    temp = t[0]
    t = t[1:] + temp
    return t

# 시계 회전 11010111
def cw(t: str):
    temp = t[-1]
    t = temp + t[:-1]
    return t

# 톱니바퀴 번호에 따른 다른 톱니 회전 파악하기
def t1_simulate(cmd):
    global ts, check
    check[1] = 1
    
    if check[2] == 0 and ts[1][2] != ts[2][6]:
        ts[2] = t2_simulate(-cmd)
        
    if cmd == 1:
        ts[1] = cw(ts[1])
    else: 
        ts[1] = ccw(ts[1])
        
    return ts[1]


def t2_simulate(cmd):
    global ts, check
    check[2] = 1

    if check[3] == 0 and ts[2][2] != ts[3][6]:
        ts[3] = t3_simulate(-cmd)
    if check[1] == 0 and ts[2][6] != ts[1][2]:
        ts[1] = t1_simulate(-cmd)
    
    if cmd == 1:
        ts[2] = cw(ts[2])
    else: 
        ts[2] = ccw(ts[2])
        
    
    return ts[2]


def t3_simulate(cmd):
    global ts, check
    check[3] = 1
    
    if check[2] == 0 and ts[3][6] != ts[2][2]:
        ts[2] = t2_simulate(-cmd)
    if check[4] == 0 and ts[3][2] != ts[4][6]:
        ts[4] = t4_simulate(-cmd)

    if cmd == 1:
        ts[3] = cw(ts[3])
    else: 
        ts[3] = ccw(ts[3])
        
    return ts[3]



def t4_simulate(cmd):
    global ts, check
    check[4] = 1 
    
    if check[3] == 0 and ts[4][6] != ts[3][2]:
        ts[3] = t3_simulate(-cmd)
        
    if cmd == 1:
        ts[4] = cw(ts[4])
    else: 
        ts[4] = ccw(ts[4])
    
    return ts[4]


for num, cmd in cmds:
    check = [0, 0, 0, 0, 0]
    if num == 1:
        t1_simulate(cmd)
    elif num == 2:
        t2_simulate(cmd)
    elif num == 3:
        t3_simulate(cmd)
    else:
        t4_simulate(cmd)

sum_val = 0
for idx, t in enumerate(ts[1:]):
    if t[0] == '1':
        sum_val += 2**(idx)
        
print(sum_val)