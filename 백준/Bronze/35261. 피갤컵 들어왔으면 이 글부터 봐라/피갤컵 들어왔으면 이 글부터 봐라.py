n = int(input())
s = input()

std = 'eagle'

answer = 10
for idx in range(0, n - len(std) + 1):
    cnt = 0
    for i in range(idx, idx + len(std)):
        if std[i - idx] != s[i]:  # 여기 수정
            cnt += 1
    answer = min(answer, cnt)
    
print(answer)