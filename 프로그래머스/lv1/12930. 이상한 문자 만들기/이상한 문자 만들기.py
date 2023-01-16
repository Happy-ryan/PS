def solution(s):
    answer = ''
    # print(list(s))
    res = [0]
    for i in range(len(s) - 1):
        if s[i] == ' ' and s[i + 1] != ' ':
            res.append(i + 1)
    res.append(len(s))
    # print(res)
    for i in range(len(res) - 1):
        a = list(s)[res[i] : res[i + 1]]
        p = 0
        for k in a:
            if k != ' ':
                if p % 2 == 0:
                    answer += a[p].upper()
                    p += 1
                else:
                    answer += a[p].lower()
                    p += 1
            else:
                answer += ' '
    return answer