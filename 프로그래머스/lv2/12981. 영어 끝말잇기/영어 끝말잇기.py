def solution(n, words):
    answer = []
    word_set = set()
    word_set.add(words[0])
    final = words[0][-1]
    i = 1 # 번호
    num, seq = 0, 0
    for word in words[1:]:
        i += 1
        num = i%n 
        if num == 0:
            num = n
        seq = i//(n) + 1
        if i%n == 0:
            seq = i//n
        if final == word[0] and word not in word_set:
            word_set.add(word)
            final = word[-1]
        else:
            final != word[-1]
            anwer = [num,seq]
            return anwer
    if len(answer) == 0:
        answer = [0,0]
    return answer
