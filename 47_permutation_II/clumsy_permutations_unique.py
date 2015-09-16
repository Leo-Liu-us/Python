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
            for num in nums:
                left_nums = nums[:]
                left_nums.remove(num)
                result.extend([num] + r for r in self.permuteUnique(left_nums))
            #remove duplicate list in result
			#the time complexity is too high
            result_unique = []
            for item in result:
            	if item not in result_unique:
            		result_unique.append(item)
            return result_unique