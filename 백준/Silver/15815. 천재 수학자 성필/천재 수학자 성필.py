arr = list(input())


def solution(arr):
    stack = []
    tmp = 0
    for x in arr:
        if not stack:
            stack.append(int(x))
        else:
            if x.isdigit():
                stack.append(int(x))
            else:
                a = stack.pop()
                b = stack.pop()
                if x == "+":
                    tmp = a + b
                elif x == "-":
                    tmp = b - a
                elif x == "*":
                    tmp = a * b
                else:
                    tmp = b // a
                stack.append(tmp)

    return tmp


print(solution(arr))