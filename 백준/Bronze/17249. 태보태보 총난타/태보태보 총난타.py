# https://www.acmicpc.net/problem/17249
s = input()
left, right = s.split("(^0^)")
print(left.count("@"), right.count("@"))