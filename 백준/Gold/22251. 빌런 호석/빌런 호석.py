N, K, P, X = map(int, input().split())

def solution(N, K, P, X):
    memo = [[0 for _ in range(10)] for _ in range(10)]
    
    nums = [[[0, 1, 0],
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1],
            [0, 1, 0]],
    
            [[0, 0, 0],
            [0, 0, 1],
            [0, 0, 0],
            [0, 0, 1],
            [0, 0, 0]],
    
            [[0, 1, 0],
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0],
            [0, 1, 0]],

            [[0, 1, 0],
            [0, 0, 1],
            [0, 1, 0],
            [0, 0, 1],
            [0, 1, 0]],

            [[0, 0, 0],
            [1, 0, 1],
            [0, 1, 0],
            [0, 0, 1],
            [0, 0, 0]],
    
            [[0, 1, 0],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [0, 1, 0]],
    
            [[0, 1, 0],
            [1, 0, 0],
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]],
    
            [[0, 1, 0],
            [0, 0, 1],
            [0, 0, 0],
            [0, 0, 1],
            [0, 0, 0]],
    
            [[0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]],
    
            [[0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
            [0, 0, 1],
            [0, 1, 0]]]
    
    def cal(num1, num2):
        r, c = len(num1), len(num1[0])
        cnt = 0
        for i in range(r):
            for j in range(c):
                if num1[i][j] != num2[i][j]:
                    cnt += 1
        return cnt
    
    for i in range(10):
        for j in range(10):
            memo[i][j] = cal(nums[i], nums[j])

    # 숫자를 디스플레이 형태로 변경하기
    def change(num: int):
        l = len(str(num))
        return '0' * (K - l) + str(num)
    
    def cal_full_number(num1: str, num2: str):
        cnt = 0
        for i in range(K):
            cnt += memo[int(num1[i])][int(num2[i])]
        return cnt
    
    # 가능한 층의 후보
    ans = 0
    # for val in range(10 ** (K - 1), 10 ** (K)):
    for val in range(1, 1000001):
        if val > N:
            continue
        num1 = change(X)
        num2 = change(val)
        cnt = cal_full_number(num1, num2)
        # print(f"num1: {num1}, num2: {num2}, cnt : {cnt}")
        if 1 <= cnt and cnt <= P:
            # print(f"num1: {num1}, num2: {num2}, cnt : {cnt}")
            ans += 1
    
    return ans

print(solution(N, K, P, X))