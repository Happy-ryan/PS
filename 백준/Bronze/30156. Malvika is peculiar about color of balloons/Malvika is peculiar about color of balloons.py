n = int(input())
for _ in range(n):
    s = input()
    a_cnt = s.count('a')
    b_cnt = s.count('b')
    print(min(a_cnt, b_cnt))