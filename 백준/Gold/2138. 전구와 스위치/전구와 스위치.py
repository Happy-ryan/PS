n = int(input())
s1 = list(input())
s2 = list(input())

orgin = s1.copy()

def flip(x):
    return str(int(x)^1)

cnt_first_choose = 0
cnt_first_no = 0
inf = int(1e9)
ans = inf

for i in range(1, n):
    if s1[i - 1] != s2[i - 1]:
        cnt_first_no += 1
        s1[i - 1] = flip(s1[i - 1])
        s1[i] = flip(s1[i])
        if i + 1 < n:
            s1[i + 1] = flip(s1[i + 1])

if s1[-1] == s2[-1]:
    ans = min(ans, cnt_first_no)

s1 = orgin
s1[0] = flip(s1[0])
s1[1] = flip(s1[1])
cnt_first_choose += 1
for i in range(1, n):
    if s1[i - 1] != s2[i - 1]:
        cnt_first_choose += 1
        s1[i - 1] = flip(s1[i - 1])
        s1[i] = flip(s1[i])
        if i + 1 < n:
            s1[i + 1] = flip(s1[i + 1])

if s1[-1] == s2[-1]:
    ans = min(ans, cnt_first_choose)


if ans == inf:
    print(-1)
else:
    print(ans)