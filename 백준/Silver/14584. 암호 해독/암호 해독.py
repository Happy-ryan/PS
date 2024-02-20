from collections import deque, defaultdict

# 26번에 원상복귀
def change(k):
    origin = list("abcdefghijklmnopqrstuvwxyz")
    
    dq = deque(origin)
    dq.rotate(-k)
    
    dic = defaultdict()
    
    for i in range(len(origin)):
        dic[dq[i]] = origin[i]
    
    return dic

def check(words, after, dic):
    ans = ''
    for x in after:
        ans += dic[x]
        
    for word in words:
        if word in ans:
            return (True, ans)
    return (False, '')
    

after = input()
t = int(input())
words = [input() for _ in range(t)]

for k in range(1, 27):
    dic = change(k)
    if check(words, after, dic)[0]:
        print(check(words, after, dic)[1])
        break