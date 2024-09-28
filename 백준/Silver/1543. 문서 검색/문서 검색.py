doc = input()
target = input()

def solutino(doc, target):
    cnt = 0
    
    idx = 0
    k1 = len(doc)
    k2= len(target)
    while idx < k1:
        check = doc[idx: idx + k2]
        if check == target:
            idx += k2
            cnt += 1
        else:
            idx += 1
            
    return cnt

print(solutino(doc, target))