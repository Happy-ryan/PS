places = [0]+list(map(int,input().split()))
x,y,r = map(int,input().split())
res = set()
for i,k in enumerate(places):
    if k == x:
        res.add(i)
    else:
        res.add(0)

if len(res) == 1:
    print(0)
else:
    res.discard(0)
    ans = [i for i in res]
    print(ans[-1])
