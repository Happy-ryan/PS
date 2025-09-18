t = int(input())

def solution(txt):
    txt = txt.replace('PO', 'PHO')
    return txt
for _ in range(t):
    txt = input()
    print(solution(txt))