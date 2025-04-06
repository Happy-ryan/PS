def solution(word):
    # 1. 모음(a, e, i, o, u) 하나 반드시 포함
    # 2. 모음 또는 자음이 3개 연속 불가
    # 3. 같은 글자 연속 불가, ee, oo만 허용
    
    def check1():
        flag = False
        for w in word:
            if w in 'aeiou':
                flag = True
        return flag
    
    def check2():
        tmp = word
        for x in 'abcdefghijklmnopqrstuvwxyz':
            if x in 'aeiou':
                tmp = tmp.replace(x, '@')
            else:
                tmp = tmp.replace(x, '#')
                
        flag = True
        for i in range(len(tmp) - 2):
            if tmp[i] == tmp[i + 1] == tmp[i + 2]:
                flag = False
        return flag
    
    def check3():
        flag = True
        for i in range(len(word) - 1):
            if (word[i] == 'e' and word[i] == word[i + 1]) or\
                (word[i] == 'o' and word[i] == word[i + 1]):
                    continue
            if word[i] == word[i + 1]:
                flag = False
        return flag
    
        
    if check1():
        if check2():
            if check3():
                return f'<{word}> is acceptable.'
    
    return f'<{word}> is not acceptable.'
    
while True:
    word = input()
    if word == 'end':
        break
    print(solution(word))