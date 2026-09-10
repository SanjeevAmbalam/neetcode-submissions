class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2: return len(nums)
        L = 0
        while L<len(nums)-1:
            R = L
            while R<len(nums):
                if nums[R]==nums[L] and R!=L:
                    nums.pop(R)
                else:
                    R+=1
            L+=1
        return len(nums)