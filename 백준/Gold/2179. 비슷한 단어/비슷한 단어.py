# 단어의 수 N (2 <= N <= 20,000)
# 단어의 길이 100이하
# Max 접두사의 개수 = 20,000 * 100 = 2,000,0000

n = int(input())
words = [input() for _ in range(n)]

def solution(n, words):
    
    # 접두사 만들기 : len(words)
    def make_prefix(word):
        prefix = []
        for i in range(len(word)):
            prefix.append(word[:i + 1])
        return prefix
    
    # 방법3) 접두사의 개수를 세서 2개 이상인 것만 확인
    from collections import Counter
    dic = Counter()
    for word in words:
        p = make_prefix(word)
        for x in p:
            dic[x] += 1
    
    max_prefix_len = 0
    for k, v in dic.items():
        if v <= 1:
            continue
        max_prefix_len = max(max_prefix_len, len(k))
        
    tmp = []
    for k, v in dic.items():
        if v <= 1:
            continue
        if max_prefix_len == len(k):
            tmp.append((k))
    
    # print(tmp)
    # 반례 찾음... > 접두사가 아니고 그냥 포함된 상태인데 그걸 체크해버리는 경우!!
    # 3
    # abcd
    # bcde
    # bcdf
    # ['bcd']
    # abcd
    # bcde
    cnt = 0
    if tmp:
        x = tmp[0]
        # 서로 다른 영단어 제시되므로 같은 것 출력 안돼.
        for word in words:
            if cnt == 2:
                return
            if x in make_prefix(word):
                print(word)
                cnt += 1
    # 공통 접두사 없으면 앞에 2개 출력
    else:
        for w in words:
            if cnt == 2:
                return
            print(w)
            cnt += 1
    
solution(n, words)