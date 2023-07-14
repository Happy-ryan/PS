def solution(a, b, c):
    if b - a == c - b:
        k = b - a
        return f"AP {c + k}"
    else:
        k = b // a
        return f"GP {c * k}"
        
while True:
	a, b, c = map(int, input().split())
	if a == 0 and b == 0 and c == 0:
		break
	print(solution(a, b, c))