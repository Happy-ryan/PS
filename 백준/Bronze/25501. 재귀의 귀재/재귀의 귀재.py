# 문자열, 팰린드롬


def recursion(s, l, r, lev):
    if l >= r:
        return (1, lev)
    elif s[l] != s[r]:
        return (0, lev)
    else:
        return recursion(s, l + 1, r - 1, lev + 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1, lev)


lev = 1
n = int(input())
for _ in range(n):
    s = input()
    print(f"{isPalindrome(s)[0]} {isPalindrome(s)[1]}")
