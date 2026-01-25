n = int(input())
s = list(input())

p_idx = []
c_idx = []

for i, ch in enumerate(s):
    if ch == 'P':
        p_idx.append(i)
    elif ch == 'C':
        c_idx.append(i)

# 짝지을 수 있는 개수
k = min(len(p_idx), len(c_idx))

for i in range(k):
    pi = p_idx[i]
    ci = c_idx[i]
    s[pi], s[ci] = s[ci], s[pi]

print(''.join(s))