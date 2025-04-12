n, m = map(int, input().split())
memo_keywords = [input() for _ in range(n)]
write_words = [list(input().split(',')) for _ in range(m)]


def solution(n, m, memo_keywords, write_words):
    
    cnt = len(memo_keywords)
    
    delete_ = []
    # 시간복잡도 : M * 10 * N
    # for words in write_words:
    #     for w in words:
    #         if w in memo_keywords:
    #             delete_.append(w)
    # 해쉬
    from collections import Counter
    memo = Counter(memo_keywords)
    write = Counter()
    # 시간복잡도 : M * 10 * 1
    for wds in write_words:
        for wd in wds:
            if wd in memo:
                memo.pop(wd)
                cnt -= 1
        print(cnt)
        

solution(n, m, memo_keywords, write_words)