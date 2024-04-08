n = int(input())
nums = list(map(int, input().split()))

def solution(n, nums):
    stack = []
    out_stack = []
    tmp = 1
    for num in nums:
        if num == tmp:
            out_stack.append(num)
            tmp += 1
        else:
            if not stack:
                stack.append(num)
            else:
                while stack and stack[-1] == tmp:
                    out_stack.append(stack.pop())
                    tmp += 1
                stack.append(num)
    
    while stack:
        out_stack.append(stack.pop())
        
    if out_stack != list(range(1, n + 1)):
        return 'Sad'
    
    return 'Nice'

print(solution(n, nums))