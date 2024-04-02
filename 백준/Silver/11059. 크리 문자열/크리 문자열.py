n = input()

def solution(n):
    # 00 이 int(input())으로 들어오면 0으로 되기 때문에 k가 2가 아니라 1이 나온다.
    k = len(str(n))
    # print(k)
    psum = [0] * (k + 1)
    # 처음부터 내 위치까지의 합
    # psum[1] = psum[0] + n[0]
    for i in range(k):
        psum[i + 1] = psum[i] + int(str(n)[i])
    # 67896789
    # 1 2 3 4
    # 7 8 9 6 = psum[5] - psum[1] = psum[3](21) - psum[1](6) + psum[5](36) - psum[3](21) = 21 - 6 + 36 - 21 = 30
    # print(psum)
    answer = 0
    for s in range(k):
        for e in range(k):
            e += 1
            if s < e and (e - s) % 2 == 0:
                mid = (e + s) // 2
                if psum[mid] - psum[s] == psum[e] - psum[mid]:
                    answer = max(answer, e - s)

    return answer


print(solution(n))