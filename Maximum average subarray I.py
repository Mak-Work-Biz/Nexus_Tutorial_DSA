class Solution:
    def findMaxAverage(self, nums, k):
        s = sum(nums[:k])
        m = s
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            if s > m:
                m = s
        return m / k

sol = Solution()
ans = sol.findMaxAverage([1,12,-5,-6,50,3], 4)
print("%.5f" % ans)
