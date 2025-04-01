people = [input().split() for _ in range(3)] 

def solution(people):
    name1 = []
    name2 = []
    
    for p, y, name in people:
        name1.append(y)
        name2.append((int(p), name))
    
    name1.sort()
    name2.sort(key=lambda x: -x[0])
    
    ans1 = ''
    for n in name1:
        ans1 += str(n)[2:]
    
    ans2 = ''
    for _, n in name2:
        ans2 += n[0]
        
    print(ans1)
    print(ans2)
    
solution(people)