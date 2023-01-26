def solution(n, words):
    
    word_set = set() # 중복단어 발생 확인 용도)
    seq = []
    for i, word in enumerate(words):

        if len(word_set) == 0: #처음이면
            final = word[-1]
            word_set.add(word)
            seq.append((1 + i % n, 1 + (i // n)))
        else:
            if final == word[0] and word not in word_set:
                word_set.add(word)
                final = word[-1]
                seq.append((1 + i % n, 1 + (i // n))) #(나의 번호, 몇 번째)
            else:
                return [1 + i % n, 1 + (i // n)]
                break
    if len(seq) == len(words):
        return [0, 0]
