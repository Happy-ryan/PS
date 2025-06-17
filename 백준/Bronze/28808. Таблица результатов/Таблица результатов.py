n, m = map(int, input().split())
cnt_solved = 0

for _ in range(n):
    s = input()
    if '+' in s:
        cnt_solved += 1

print(cnt_solved)