t = int(input())

def solution(nums):

        
    def isPrime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            
            i = 3
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 2
            return True
    
    nums = nums[1:]

    size = len(nums)
    
    psum = [0] * (size + 1)
    for i in range(size):
        psum[i + 1] = psum[i] + nums[i]
        
    inf = int(1e18)
    
    val = (inf, inf)
    
    for w in range(2, size + 1):
        for i in range(0, size - w + 1):
            a = psum[i + w] - psum[i]
            # print(f"i: {i}, i + w : {i + w}, psum : {a}")
            if isPrime(a):
                val = min(val, (w, i))
                
    if val[0] == inf:
        return 'This sequence is anti-primed.'
    
    answer = ''
    for i in range(val[1], val[1] + val[0]):
        answer += str(nums[i]) + ' '
    
    return f"Shortest primed subsequence is length {val[0]}: {answer}"
    
    
for _ in range(t):
    nums = list(map(int, input().split()))
    print(solution(nums))