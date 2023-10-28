s = input()
n = len(s)
# s[i] ~ s[j]까지의 문자열이 팰린드롬인지 확인용!
is_palindrome = [[False for _ in range(n)] for _ in range(n)]

# 1자리 - 팰린드롬
# reversed ?
# is_palindrome[l+1][r-1] || is_palindrome[l][r]
# reversed가 없어..l = 0 ~ r = x <= l = 1 ~ r = x - 1 알 수 없어...
# reversed (n - 7, n - 4) <= (n - 6, n - 5) 알고있음!
for l in reversed(range(n)):
    is_palindrome[l][l] = True
    if l + 1 < n and s[l] == s[l+1]:
        is_palindrome[l][l+1] = True
    for r in range(l+2, n):
        if is_palindrome[l+1][r-1] and s[l] == s[r]:
            is_palindrome[l][r] = True

# dp[i]의 I am 정의: s[i]번째까의 팰린드롬 분할의 최소 수
dp = [i+1 for i in range(n)]
# [ 수 많은 팰린드롬 존재 j /j + 1 마지막 팰린드롬] + s[i] => 팰린드롬 s[j+1][i] 이냐?!
for i in range(n):
    if is_palindrome[0][i]:
        dp[i] = 1
    for j in range(i):
        if is_palindrome[j+1][i]:
            dp[i] = min(dp[i], dp[j] + 1)

print(dp[n-1])