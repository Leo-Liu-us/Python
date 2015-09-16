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
                for item in self.permuteUnique(left_nums):
                	permute_item = [num] + item
					#check whether it already exists
                	if permute_item not in result:
                		result.append(permute_item)
                		
            return result