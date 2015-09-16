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
        print nums
        return self.helper(nums, k)
        
    def helper(self, nums, k):
        result = []
        if k == 1:
            for num in nums:
                result.append([num])
            return result
        else:
            for num in nums:
                left_nums = nums[:]
                left_nums.remove(num)
                for r in self.helper(left_nums, k-1):
                    result.append([num] + r)
            return result