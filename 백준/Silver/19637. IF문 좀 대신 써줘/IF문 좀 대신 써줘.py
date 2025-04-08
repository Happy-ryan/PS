n, m = map(int, input().split())
conditions = [list(input().split()) for _ in range(n)]
qs = [int(input()) for _ in range(m)]

# 정렬해도 상관없으면 정렬해버리자!!!!
# 정렬 이야기 나오면 이분탐색!!!!

def solution(n, m, conditions, qs):
    
    # qs > 시간복잡도 O(M) = 10^5 <- 쿼리를 돌아야하므로 무조건 발생하는 복잡도
    # conditions > q에 따라 conditions for문 돌면서 찾으면 O(N) = 10^5 <- 터짐

    # q가 들어왔을 때 conditon을 바로 판단할 수 있어야함 <- 시간복잡도 내려야함,, / 이분탐색
    
    def binary(q):
        l, r = 0, n - 1 # 답의 범위 생각하기
        while l <= r:
            m = (l + r) // 2
            _, v = conditions[m]
            v = int(v)
            if v < q:
                l = m + 1
            else:
                r = m - 1
        return conditions[l][0]

    for q in qs:
        print(binary(q))


solution(n, m, conditions, qs)     