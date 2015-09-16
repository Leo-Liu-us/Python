class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        else:
            result = []
            for num in nums:
                left_nums = nums[:]
                left_nums.remove(num)
                result.extend([num] + r for r in self.permute(left_nums))
            return result