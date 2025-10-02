class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxarea = 0

        while left < right:
            width = right - left
            length = min(height[right], height[left])
            area = width * length

            maxarea = max(area, maxarea)

            if height[right] > height[left]:
                left +=1
            else:
                right -=1
