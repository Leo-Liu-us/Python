class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        #copy nums1 to a new array
        tmp_nums = nums1[:]
        tmp_idx, nums1_idx, nums2_idx = 0, 0, 0
        
        while tmp_idx in range(0, m) and nums2_idx in range(0, n):
            if tmp_nums[tmp_idx] < nums2[nums2_idx]:
                nums1[nums1_idx] = tmp_nums[tmp_idx]
                tmp_idx += 1
            else:
                nums1[nums1_idx] = nums2[nums2_idx]
                nums2_idx += 1
            nums1_idx += 1
            
        #add the remaining part
        if tmp_idx == m:
            nums1[nums1_idx:m+n] = nums2[nums2_idx:n]
        else:
            nums1[nums1_idx:m+n] = tmp_nums[tmp_idx:m]