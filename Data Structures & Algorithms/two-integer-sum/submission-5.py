class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            other_num = target - value
            if other_num in seen:
                return [seen[other_num], i]
            seen[value] = i # {num: index}