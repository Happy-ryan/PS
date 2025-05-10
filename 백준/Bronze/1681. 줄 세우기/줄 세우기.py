N, L = map(int, input().split())

def solution(N, L):
    
    L = str(L)
    nums = []
    x = 1
    while len(nums) != N:
        if L not in str(x):
            nums.append(x)
        x += 1
    
    return nums[-1]

print(solution(N, L))