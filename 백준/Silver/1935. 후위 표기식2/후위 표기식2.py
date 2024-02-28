n = int(input())
s = input()
nums = [int(input()) for _ in range(n)]

def solution(n, s, nums):
    stack = []
    # 후위연산자는 연산자 앞에 숫자 2개를 가지고 연산하고 나서 그 결과를 스택에 넣음!
    
    dic = {}
    arr = ''
    for x in s:
        if x not in  '*/+-' and x not in arr:
            arr += x
    for idx, x in enumerate(arr):
        dic[x] = nums[idx]
        
    for x in s:
        if x in "*/+-":
            # stack은 마지막이 최근숫자다!
            x2 = stack.pop()
            x1 = stack.pop()
            if x == "*":
                stack.append(x1 * x2)
            elif x == "+":
                stack.append(x1 + x2)
            elif x == "-":
                stack.append(x1 - x2)
            else:
                stack.append(x1 / x2)
        else:
            stack.append(dic[x])

    ans = stack.pop()
    return f"{ans:.2f}"


print(solution(n, s, nums))