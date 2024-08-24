n = int(input())
s = input()

t_cnt = s.count('t')
s_cnt = s.count('s')

idx = 0

while idx < n:
    if t_cnt == s_cnt:
        print(s[idx:])
        break
    idx += 1
    if s[idx - 1] == 's':
        s_cnt -= 1
    else:
        t_cnt -= 1