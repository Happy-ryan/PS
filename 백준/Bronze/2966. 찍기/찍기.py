n = int(input())
ans = list(input())

def solution(ans, my_ans, name):
    idx = 0
    cnt = 0
    
    for x in ans:
        if x == my_ans[idx]:
            cnt += 1 
        idx = (idx + 1) % len(my_ans)
    
    return (name, cnt)

p1, c1 =  solution(ans, 'ABC', 'Adrian')
p2, c2 = solution(ans, 'BABC', 'Bruno')
p3, c3 = solution(ans, 'CCAABB', 'Goran')

max_ans = max(c1, c2, c3)

print(max_ans)
for p, c in [(p1, c1), (p2, c2), (p3, c3)]:
    if c == max_ans:
        print(p)