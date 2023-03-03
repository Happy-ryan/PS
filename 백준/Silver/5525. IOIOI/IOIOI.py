# 문자열
# 시간복잡도 주의

n = int(input())
m = int(input())
s = input()

p = f"I{'OI' * n}"
cnt = 0


def check(start, p, s):
    global cnt
    k = len(p)
    if s[start : start + k] == p:
        cnt += 1


for start in range(len(s) - len(p) + 1):
    check(start, p, s)

print(cnt)
