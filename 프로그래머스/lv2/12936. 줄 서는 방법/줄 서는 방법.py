def fact(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = i * dp[i - 1]
    
    return dp[n]
    
def solution(n, k):
    answer = []
    used = [0] * (n + 1) # 숫자 사용 확인 용도
    
    for i in range(0, n):
        after = fact(n - i - 1)
        for x in range(1, n + 1):
            if used[x] == 0:
                if after < k: # after안에 k가 없다. 즉 지금 x로는 k번째 표현 불가능
                    k -= after # 규칙 : after만큼 생성
                else:
                    answer.append(x)
                    used[x] = 1
                    break #현재 인덱스i에 x가 들어갔으니까 x에 대한 for문 탈출
                    
    return answer