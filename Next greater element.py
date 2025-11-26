class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}
        
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
        
        return [next_greater.get(x, -1) for x in nums1]
