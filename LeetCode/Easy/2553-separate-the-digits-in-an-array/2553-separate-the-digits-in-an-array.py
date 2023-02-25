class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = ''
        for x in nums:
            res += str(x)
        return list(map(int, res))
            