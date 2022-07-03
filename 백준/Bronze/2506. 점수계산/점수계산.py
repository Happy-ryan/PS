n = int(input())
arr = list(input().split())
score = 0
hap = 0
for x in arr:
    if x == '1':
        hap +=1
        score += hap
    else:
        hap = 0 # 1이 아니면 hap 초기화

print(score)