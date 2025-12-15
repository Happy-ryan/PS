A = input()
B = input()

def solution(A, B):
    
    ans1, ans2, ans3, ans4 =  '', '', '', ''
    
    def AND(a, b):
        ans = ''
        for i in range(len(a)):
            if a[i] == '1' and b[i] == '1':
                ans += '1'
            else:
                ans += '0'
        return ans
    
    def OR(a, b):
        ans = ''
        for i in range(len(a)):
            if a[i] == '1' or b[i] == '1':
                ans += '1'
            else:
                ans += '0'
        return ans
    
    def XOR(a, b):
        ans = ''
        for i in range(len(a)):
            if a[i] != b[i]:
                ans += '1'
            else:
                ans += '0'
        return ans
    
    def NOT(a):
        ans = ''
        for i in range(len(a)):
            if a[i] == '1':
                ans += '0'
            else:
                ans += '1'
        return ans
    
    return AND(A, B), OR(A, B), XOR(A, B), NOT(A), NOT(B)

ans = solution(A, B)
for a in ans:
    print(a)