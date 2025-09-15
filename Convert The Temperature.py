class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        kelvin = celsius +273.15
        ans.append(round(kelvin,5))
        fah = celsius *1.8 +32.0
        ans.append(round(fah,5))
        return ans
