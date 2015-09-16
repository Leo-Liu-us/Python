class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []
        nums = range(1, n+1)
        return self.helper(nums, k)
        
    def helper(self, nums, k):
        result = []
        if k == 1:
            for num in nums:
                result.append([num])
            return result
        else:
            for idx, num in enumerate(nums):
                left_nums = nums[idx+1:]
                for r in self.helper(left_nums, k-1):
                    result.append([num] + r)
            return result