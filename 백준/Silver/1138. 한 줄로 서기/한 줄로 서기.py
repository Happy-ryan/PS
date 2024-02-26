n = int(input())
nums = list(map(int, input().split()))

def solution_2(n, nums):
    # 내가 숫자를 넣으면 내 오른쪽 값들은 0을 하나씩 잃어버림
    # 나의 인덱스(idx) + 1 ~ n, 즉 내 오른쪽에서 0을 하나씩 제외할 것
    
    memo = list(range(n))
    check = [0] * n
    
    answer = [0] * n
    for high, num in enumerate(nums):
        
        for i in range(n):
            if memo[i] == num and check[i] == 0:
                idx = i
                
        answer[idx] = high + 1
        check[idx] = 1
        
        # 0을 제외하는 작업!
        for x in range(idx + 1, n):
            if check[x] == 0:
                memo[x] -= 1
                
    return answer

print(*solution_2(n, nums))