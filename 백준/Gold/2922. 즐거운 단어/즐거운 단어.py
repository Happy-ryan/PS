def is_3time(words):
    voewl = "AEIOU"

    if "L" not in words:
        return False

    cnt_vovewl = 0
    cnt_consonant = 0
    for word in words:
        if word in voewl:
            cnt_vovewl += 1
            cnt_consonant = 0
        else:
            cnt_consonant += 1
            cnt_vovewl = 0
        if cnt_vovewl == 3 or cnt_consonant == 3:
            return False
    return True

def make_word(s: str, ans: list[str]):
    for x in ans:
        s = s.replace("_", x, 1)
    return s

def calculate(ans):
    res = 1
    for x in ans:
        if x == "A":
            res *= 5
        elif x == "B":
            res *= 20
        else:
            res *= 1
    return res

s = input()
ans = []
# alpabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 전수를 구하면 시간초과..결국 경우의 수를 구하기 때문에 대표되는 알파벳만 넣고 곱하자
alpabet = {"voewl" : "A", "consonant" : "B", "must" : "L"}
ans = []
n = s.count("_")
cnt = 0

def dfs(level):
    global s, cnt
    if level == n:
        res = make_word(s, ans.copy())
        if is_3time(res):
            cnt += calculate(ans)
            # print(f"ans: {ans}, res: {res}, cnt: {ans}")
        return
    for al in alpabet.values():
        ans.append(al)
        dfs(level + 1)
        ans.pop()

dfs(0)
print(cnt)