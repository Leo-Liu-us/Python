class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            yield nums
        else:
            for num in nums:
                left_nums = nums[:]
                left_nums.remove(num)
                for r in self.permute(left_nums):
                	yield [num] + r

items = [1,2,3]
for i in Solution().permute(items):
	print i