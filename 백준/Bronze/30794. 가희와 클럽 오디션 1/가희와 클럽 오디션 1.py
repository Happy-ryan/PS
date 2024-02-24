def solution(level, result):
    if result == "miss":
        return 0
    if result == "bad":
        return level * 200
    if result == "cool":
        return level * 400
    if result == "great":
        return level * 600
    return level * 1000


level, result = input().split()
print(solution(int(level), result))