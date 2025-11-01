class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i,j = 0, int(math.sqrt(c))
        while i <= j:
            total = i**2 + j**2
            if total == c:
                return True
            elif total < c:
                i +=1
            else:
                j-=1
        return False
    
        
