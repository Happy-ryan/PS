def solution(n):
    for k in range(n+1, 1000000):
        n_bin = bin(n)[2:]
        k_bin = bin(k)[2:]
        if n_bin.count('1') == k_bin.count('1'):
            answer = k
            break
    return answer