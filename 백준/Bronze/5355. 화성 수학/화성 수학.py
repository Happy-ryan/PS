def solution(t, cases):
    answer = []
    for case in cases:
        num, cmds = float(case[0]), case[1:]
        for cmd in cmds:
            if cmd == '@':
                num *= 3
            elif cmd == '%':
                num += 5
            elif cmd == '#':
                num -= 7
        answer.append(f"{num:.2f}")
    return answer

t = int(input())
cases = [list(input().split()) for _ in range(t)]
for row in solution(t, cases):
    print(row)