# https://www.acmicpc.net/problem/6198
n = int(input())
highs = [int(input()) for _ in range(n)]

stack = []
cnt_record = [0] * (n)
for idx, high in enumerate(highs):
    while stack:
        if stack[-1][1] <= high:
            stack.pop()
        else:
            #나를 볼 수 있는 사람들의 수를 의미함
            cnt_record[idx] = cnt_record[stack[-1][0]] + 1
            break
        
    stack.append((idx, high))
            
#print(cnt_record)
print(sum(cnt_record))