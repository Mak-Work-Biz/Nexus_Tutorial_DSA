class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output = []
        nums_sorted = sorted(nums)
        for index,num in enumerate(nums_sorted):
            if num == target:
                output.append(index)

        return output
