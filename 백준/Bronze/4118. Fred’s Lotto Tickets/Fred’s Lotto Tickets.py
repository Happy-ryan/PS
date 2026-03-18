from collections import Counter

def solution(n, nums):
    dic = Counter()
    
    for num_row in nums:
        for num in num_row:
            if num not in dic:
                dic[num] += 1
                             
    if sum(dic.values()) == 49:
        return 'Yes'
    
    return 'No'


while True:
    n = int(input())
    
    if n == 0: break
    
    nums = [list(map(int, input().split())) for _ in range(n)]
    
    print(solution(n, nums))