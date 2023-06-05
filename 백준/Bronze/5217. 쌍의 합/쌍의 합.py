# https://www.acmicpc.net/problem/5217
def solution(num: int):
    ans = []
    for x in range(1, num//2 + 1):
        if x * 2 == num:
            continue
        else:
            ans.append((x, num - x))
    ans.sort(key= lambda x: (x[0], x[1]))
    final = f"Pairs for {num}: "
    for i in range(len(ans)):
        if i == len(ans) -1:
            final += f"{ans[i][0]} {ans[i][1]}"
        else:
            final += f"{ans[i][0]} {ans[i][1]}, "
        
    return final

t = int(input())
for _ in range(t):
    n = int(input())
    print(solution(n))