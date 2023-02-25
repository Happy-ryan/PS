class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        def sum_digit(number):
        
            if number < 10: # 종료조건
                return number
    
            return (number % 10) + sum_digit(number // 10)
        
        x1 = sum(nums)
        
        x2 = 0
        for k in nums:
            x2 += sum_digit(k)
    
        return abs(x1 - x2)
        