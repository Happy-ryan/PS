class Solution:
    def alternateDigitSum(self, n: int) -> int:
        cnt = 0
        for i, x in enumerate(str(n)):
            if i % 2 == 0:
                cnt += int(x)
            else:
                cnt -= int(x)
        return cnt
        