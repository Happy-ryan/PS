a = input()
b = input()
ab = ''

for i in range(len(a)):
    ab += a[i] + b[i]

def f(s):
    ans = '' # ans을 함수 밖으로 하면 초기화가 안 되고 계속 누적만 된다.
    if len(s) == 2: # 재귀 탈출 조건
        print(s)
        return
    for i in range(0, len(s) - 1):
        row = 0
        for x in s[i : i + 2]:
            row += int(x)

        if row < 10:
            row = str(row)
        else:
            row = str(row)[1]
        ans += row

    f(ans)

f(ab)