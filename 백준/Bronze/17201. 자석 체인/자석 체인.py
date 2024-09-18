n = int(input())
magnetics = input()

def solution(n, magnetics):
    ms = []
    for x in magnetics:
        if not ms:
            ms.append(x)
        else:
            if ms[-1] == x:
                return "No"
            else:
                ms.append(x)
    return "Yes"


print(solution(n, magnetics))