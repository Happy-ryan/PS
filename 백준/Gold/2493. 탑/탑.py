# # https://www.acmicpc.net/problem/2493
# # 시간복잡도: 이중for문 > O(n^2)

n = int(input())
tops = list(map(int, input().split()))

stack = []
res = [0] * n

for idx, nxt_top in enumerate(tops):
    while stack:
        # 스택의 마지막 탑과 nxt_top을 비교했을 때 nxt_top이 더 크면
        # 스택의 마지막 탑, 즉 좌측 탑은 전혀 볼 필요가 없다! 
        # 그러므로 nxt_top이 더 크면 좌측의 탑을 전부 빼도 상관없다.
        if stack[-1][0] < nxt_top:
            stack.pop()
        else:
            res[idx] = stack[-1][1] + 1
            break
        
    stack.append((nxt_top, idx))
    
print(*res)