class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for idx in range(k):
            heapq.heappush(heap, nums[idx])
            
        #for the remaining, compare with the top
        for i in nums[k:]:
            if i > heap[0]:
                heapq.heapreplace(heap, i)
        
        return heap[0]