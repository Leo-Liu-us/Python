class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        new_idx, old_idx = 0, 0
        nums_len = len(nums)
		
        while old_idx < nums_len:
            if nums[old_idx] != val:
                nums[new_idx] = nums[old_idx]
                new_idx += 1
            old_idx += 1
        return new_idx