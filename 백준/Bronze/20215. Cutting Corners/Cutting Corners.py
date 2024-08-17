w, h = map(int, input().split())
# w + h : 직사각형 자르기
# (w ** 2 + h ** 2) ** 0.5 : 대각선 자르기
ans = w + h - (w ** 2 + h ** 2) ** 0.5
print(ans)