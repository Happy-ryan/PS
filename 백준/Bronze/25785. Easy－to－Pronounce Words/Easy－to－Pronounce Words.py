# https://www.acmicpc.net/problem/25785
# 단어의 모든 모음 바로 뒤에 자음이 오고 모든 자음 바로 뒤에 모음이 오는 경우 단어를 발음하기 쉬운 것으로 정의합니다
# 모음 :a i o e u

def sol(s:str):
    vowels = ["a", "i", "o", "e", "u"]
    conso = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    flag = True
    for idx, x in enumerate(s):
        if idx == len(s) - 1 or not flag:
            if flag:
                return 1
            else:
                return 0
        
        if x in vowels:
            if s[idx + 1] not in conso:
                flag = False
        else:
            if s[idx + 1] not in vowels:
                flag = False
                
                
print(sol(input()))

