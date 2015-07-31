class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        start, end, sum = 0, 0, 0
        length = len(nums)
        
        for start in range(0, length):
            sum = 0
            for end in range(start, length):
                sum += nums[end]
                if sum == 0:
                    return start, end