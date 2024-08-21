n = int(input())
tops = [int(input()) for _ in range(n)]

def solution(tops):
    cnt = 0
    stack = []
    
    for top in tops:
        if not stack:
            stack.append(top)
        else:
            if stack[-1] < top:
                stack.append(top)
            
    return len(stack)

print(solution(tops))
print(solution(tops[::-1]))