# https://www.acmicpc.net/problem/18312
n, k = map(int, input().split())
# 00시 00분 00초부터 N시 59분 59초

# 전체 경우의 수 24 * 60 * 60 < 86400

sum_val = 0
for h in range(0, n + 1):
    for m in range(0, 60):
        for s in range(0, 60):
            # if str(k) not in str(h) and\
            #     str(k) not in str(m) and\
            #     str(k) not in str(s):
            #     sum_val += 1
            # 틀린 이유 : 0이 문제다. h : m : s => 23 : (0)1 : (0)1
            
            # 0으로 패딩!
            ans = f"{h:02}{m:02}{s:02}"
            if ans.find(str(k)) != -1:
                sum_val += 1

print(sum_val)
