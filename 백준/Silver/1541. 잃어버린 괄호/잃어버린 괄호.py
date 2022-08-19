S = input().split('-')
# print(S)
result = [0] * len(S)
for i in range(len(S)):
    if '+' not in S[i]:
        result[i] += int(S[i])
    else:
        SS = S[i].split('+')
        for k in SS:
            result[i] += int(k)

# print(result)
if len(result) == 1:
    print(result[0])
else:
    cnt = result[0]
    for x in result[1:]:
        cnt -= x
    print(cnt)