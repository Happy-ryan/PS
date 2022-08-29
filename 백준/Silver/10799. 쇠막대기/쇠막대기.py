arr = list(input())
stack = []
ans = 0
for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(1)
    elif arr[i] == ')' and arr[i-1] == '(':
        stack.pop()
        ans += sum(stack)
    else:
        stack.pop()
        ans += 1
    
print(ans)