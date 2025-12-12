def solution(text, pattern):
    
    m = len(pattern)
    lps = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j-1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                return True
    return False


s = input().strip()
k = input().strip()

new_s = ''.join(c for c in s if not c.isdigit())

print(1 if solution(new_s, k) else 0)
