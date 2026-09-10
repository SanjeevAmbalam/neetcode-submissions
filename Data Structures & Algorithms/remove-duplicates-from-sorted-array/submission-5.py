class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        if len(nums) < 2: return len(nums)
        while i<len(nums):
            if nums[i]==nums[i-1]:
                nums.pop(i)
            else:
                i+=1
            
        return len(nums)