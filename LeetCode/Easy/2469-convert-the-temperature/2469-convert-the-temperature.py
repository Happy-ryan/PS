class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        k = celsius + 273.15
        f = celsius * 1.8 + 32.00
        # round(실수, 표현할 소수점 자리)
        return [round(k, 5), round(f, 5)]