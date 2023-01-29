t = int(input())

def cal(x):
    y = len(x)//2
    if x[y - 1] == x[y]:
        return 'Do-it'
    else:
        return 'Do-it-Not'

for _ in range(t):
    x = input()
    print(cal(x))