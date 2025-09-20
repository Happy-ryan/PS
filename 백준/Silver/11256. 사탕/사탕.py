t = int(input())

def solution(J, N, boxs):
    # 정렬해도 무관 -> 박스의 크기 순으로 정렬
    boxs.sort(key=lambda x : -(x[0] * x[1]))
    
    idx = 0
    cnt = 0
    while J > 0:
        x,  y = boxs[idx]
        if J > x * y:
            J -= x * y
        else:
            J = 0
        idx += 1
        cnt +=1
        # print(f"cnt: {cnt}, x: {x}. y : {y}")
        
    return cnt

for _ in range(t):
    J, N = map(int, input().split())
    boxs = [list(map(int, input().split())) for _ in range(N)]
    print(solution(J, N, boxs))