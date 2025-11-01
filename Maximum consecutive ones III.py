class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j=0
        for a in range(len(nums)):
            if nums[a] == 0:
                if k > 0:
                    k-=1
                else:
                    while nums[j] != 0:
                        j+=1
                    j+=1
            i = max(i,a-j+1)
        return i
