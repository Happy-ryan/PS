n = int(input())

def solution(n):
    
    nums = [1]
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            nums.append(i)
            if i ** 2 != n:
                nums.append(n // i)
            
    nums.append(n)
    
    # print(nums)
    
    return sum(nums)

print(solution(n))