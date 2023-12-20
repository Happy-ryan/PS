# https://www.acmicpc.net/problem/16120

s = input()
# PPAP가 되면 P가 된다!
# stack에서 올바른 괄호 만나면 사라지는 것과 유사해보임!
stack = []

for x in s:
    if len(stack) < 4:
        stack.append(x)
    else:
        if stack[-4:] == ["P","P","A","P"]:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append("P")
        stack.append(x)


if stack == ["P", "P", "A", "P"] or stack == ["P"]:
    print("PPAP")
else:
    print("NP")