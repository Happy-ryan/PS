k = input()
n = int(input())
arr = [input() for _ in range(n)]

def solution(k, n, arr):
    
    cnt = 0
    answer = []
    for a in arr:
        flag = True
        for i in range(9):
            if k[i] == '*':
                continue
            if k[i] != a[i]:
                flag = False
                break
        if flag:
            answer.append(a)
            cnt += 1
    
    print(cnt)
    for row in answer:
        print(''.join(row))

solution(k, n, arr)