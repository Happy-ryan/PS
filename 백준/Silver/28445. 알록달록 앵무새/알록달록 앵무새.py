b1, t1 = input().split()
b2, t2 = input().split()

def solution(b1, t1, b2, t2):
    
    arr = set()
    for b in [b1, t1, b2, t2]:
        for t in [b1, t1, b2, t2]:
            arr.add(b + ' ' + t)
    
    arr = list(arr)
    
    arr.sort(key= lambda x: (x.split(' ')[0], x.split(' ')[1]))
    
    return arr


for x in  solution(b1, t1, b2, t2):
    print(x)