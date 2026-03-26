n = int(input())
words = [input() for _ in range(n)]
m = int(input())
candidates = [input() for _ in range(m)]

def solution(n, words, m, candidates):
    
    if n == 1:
        return candidates[0]
    
    idx = 0
    for i, word in enumerate(words):
        if word == '?':
            idx = i
    
    ba = []
    if idx == 0:
        ba.append(words[idx + 1])
    elif idx == n - 1:
        ba.append(words[idx - 1])
    else:
        ba.append(words[idx - 1])
        ba.append(words[idx + 1])
        
    for can in candidates:
        if can in set(words):
            continue
        if idx == 0:
            # ? (word)
            if ba[0][0] == can[-1]:
                return can
            # (word) ?
        elif idx == n - 1:
            if ba[0][-1] == can[0]:
                return can
        else: # (word1) ? (word2)
            if ba[0][-1] == can[0]  and ba[1][0] == can[-1]:
                return can
    
print(solution(n, words, m, candidates))