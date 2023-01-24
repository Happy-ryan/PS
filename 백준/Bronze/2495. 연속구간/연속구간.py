def check(s):
    ans = 0
    stack = []
    for x in s:
        if len(stack) == 0:
            stack.append(x)
        else:
            if stack[-1] != x:
                stack.append('/')
                stack.append(x)
            else:
                stack.append(x)
    a = ''.join(stack).split('/')
    for x in a:
        ans = max(ans, len(x))
    return ans

for _ in range(3):
    s = input()
    print(check(s))
