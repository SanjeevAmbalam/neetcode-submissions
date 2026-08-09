class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            other_num = target - nums[i]
            if other_num in seen:
                return [seen[other_num], i]
            seen[nums[i]] = i # {num: index}


