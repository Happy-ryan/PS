# https://www.acmicpc.net/problem/17294

def checkCuteNumber(n: list[int]):
    if len(n) == 1:
        return '◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!'
    else:
        k = n[0] - n[1]
        for i in range(len(n) - 1):
            if n[i] - n[i + 1] != k:
                return '흥칫뿡!! <(￣ ﹌ ￣)>'
        else:
            return '◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!'

n = list(map(int, list(input())))
result = checkCuteNumber(n)
print(result)