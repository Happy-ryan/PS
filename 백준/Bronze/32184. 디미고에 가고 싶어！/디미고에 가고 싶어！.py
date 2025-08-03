a, b = map(int, input().split())

cnt = 0
# a는 짝수 / b는 홀수일때 각각 이슈
if a % 2 == 0 and b % 2 == 0:
    cnt += (b - (a + 1) + 1) // 2 
    cnt += 1 # a 홀수
elif a % 2 == 0 and b % 2 != 0:
    cnt += ((b - 1) - (a + 1) + 1) // 2 
    cnt += 1 # a 짝수
    cnt += 1 # b 홀수
elif a % 2 != 0 and b % 2 == 0:
    cnt += (b - a + 1) // 2
elif a % 2 != 0 and b % 2 != 0:
    cnt += ((b - 1) - a + 1) // 2
    cnt += 1 # b 홀수

print(cnt)