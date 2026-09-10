class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for non_dup_index in range(len(nums)):
            check_index = non_dup_index + 1
            for i in range(non_dup_index + 1, len(nums)):
                if check_index < len(nums) and nums[non_dup_index] == nums[check_index] :
                    nums.pop(check_index)
                    check_index = non_dup_index + 1
                else:
                    check_index += 1
        return len(nums)

            