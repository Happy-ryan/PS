n = int(input())
nums = list(map(int, input().split()))

# 내 앞의 0의 개수!!
def solution(n, nums):
    # 작은 값부터 채우기때문에 내 왼쪽의 0의 개수가 곧 나보다 큰 수를 의미하며, 곧 num을 의미한다.
    memo = [0] * (n)
    for idx, num in enumerate(nums):
        s = 0
        cnt = 0 # 0의 개수
        #print(f"idx: {idx + 1}, num: {num}, cnt: {cnt}")
        while s < n:
            if cnt == num:
                if memo[s] == 0:
                    memo[s] = idx + 1
                    break
                else:
                    s += 1
            
            elif memo[s] == 0:
                cnt += 1
                s += 1
            else:
                s += 1
        #print(f"memo: {memo}")
        #print("=")
    return memo

print(*solution(n, nums))