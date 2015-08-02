class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        #len(nums) = 0, 1, 2 case
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0
        elif len( nums) == 2:
            #either descending or ascending
            if nums[0] < nums[1]:
                return 1
            else:
                return 0
        #len(nums) > 2
        start, end = 0, len(nums)
        mid = start + (end-start)/2
        #judge whether nums[mid] is peak
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        else:
            #case 1: nums[mid-1] < nums[mid] < nums[mid+1]
            if nums[mid-1] < nums[mid] and nums[mid] < nums[mid+1]:
                if nums[start] < nums[mid]:
                    return mid + self.findPeakElement(nums[mid:])
                else:
                    return self.findPeakElement(nums[:mid-1])
                    
            #case 2: nums[mid-1] > nums[mid] < nums[mid+1]
            if nums[mid-1] > nums[mid] and nums[mid] < nums[mid+1]:
                return mid + self.findPeakElement(nums[mid:])
            
            #case 3: nums[mid-1] > nums[mid] > nums[mid+1]
            if nums[mid-1] > nums[mid] and nums[mid] > nums[mid+1]:
                return self.findPeakElement(nums[start: mid+1])