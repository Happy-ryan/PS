# https://www.acmicpc.net/problem/2712


def f(s: str):
    dic = {
        'E': 'I',
        'S': 'N',
        'T': 'F',
        'J': 'P',
        "I": 'E',
        'N': 'S',
        'F': 'T',
        'P': 'J'
    }
    ans = ''
    for x in s:
        ans += dic[x]
    return ans

print(f(input()))
    