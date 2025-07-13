n = int(input())
names = [input() for _ in range(n)]

def solution(n, names):
    
    names.sort(key=lambda x : (len(x), x))
    
    for name in names:
        if len(name) == 3:
            return name
    

print(solution(n, names))