class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        start, end = 0, len(nums)
        
        #case 1: ascending list
        if nums[start] <= nums[end-1]:
            return nums[start]
        else:
            #case 2: ascending first, break, ascending again
            while(start < end):
                mid = start + (end-start)/2
                if nums[mid] > nums[start]:
                    start = mid
                else:
                    if nums[mid-1] > nums[mid]:
                        return nums[mid]
                    else:
                        end = mid