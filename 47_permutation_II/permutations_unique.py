class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        else:
            result = []
            chosed = {}
            for num in nums:
				# for each num, check and record whether it has been chosen.
            	if num in chosed:
            		continue
            	chosed[num] =True
                left_nums = nums[:]
                left_nums.remove(num)
                result.extend([num] + r for r in self.permuteUnique(left_nums))
            return result