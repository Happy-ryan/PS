n, k = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(n)]

def solution(n, k, infos):
    # info = (Ai, Bi)
    # Ai = 제시한 입찰 가격 / Bi = 제시한 입찰가 외 최고 입찰가
    # Ai > Bi 입찰!!!
    arr = [0]
    cnt = 0
    for info in infos:
        A_i, B_i = info
        if A_i >= B_i:
            cnt += 1
        else:
            # 입찰가의 차이 기록
            arr.append(B_i - A_i)
    # 최소로 올리기 위함.
    arr.sort()
    # '더' 필요한 낙찰의 수
    final = k - cnt
    if final <= 0:
        return 0
    return arr[final]

print(solution(n, k, infos))