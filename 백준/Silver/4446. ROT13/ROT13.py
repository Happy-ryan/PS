import sys

V1 = ['a', 'i', 'y', 'e', 'o', 'u']
V2 = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']

def transfer(char):
    if char in V1:
        idx = V1.index(char)
        return V1[(idx + 3) % 6]  # 복호화 = 다시 오른쪽 3칸
    elif char in V2:
        idx = V2.index(char)
        return V2[(idx + 10) % 20]  # 복호화 = 다시 오른쪽 10칸
    return char

for line in sys.stdin:
    answer = ''
    for char in line.rstrip('\n'):
        if char.isupper():
            answer += transfer(char.lower()).upper()
        else:
            answer += transfer(char)
    print(answer)