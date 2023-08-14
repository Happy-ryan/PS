def f(s1: str):
    ans = []
    password = ["A", "B", "C", "D", "E", "F", "G", "H"]
    promise = ['000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010']
    for x in promise:
        check = 0
        for x1, x2 in zip(x, s1):
            if x1 == x2:
                continue
            check += 1
        if check <= 1:
            ans.append(x)
            
    if len(ans) == 1:
        idx = promise.index(ans[-1])
        return password[idx]
    else:
        False
        
n = int(input())
s1 = input()
ans = ''
flag = True
for i in range(0, len(s1), 6):
    k =f(s1[i:i+6])
    if k:
        ans += k 
    else:
        flag = False
        ans = i//6 + 1
        break    

print(ans)