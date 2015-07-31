class Solution:
    # @param {integer[]} nums
    # @return a tuple, (found, [(b0,c0),(b1,c1)...])
    # @ the first element is flag whether found or not
    # @ the second element is a set contains all pairs
    def twoSum(self, nums, twoSum):
        pairs_set = set()
        val = {}
        found = False
        
        #trasverse nums once
        #get all the pairs which have the sum
        #do not include duplicate pair
        for first in nums:
            second = twoSum - first
            if second in val:
                found = True
                b = min(first, second)
                c = max(first, second)
                new_pair = (b, c)
                if new_pair not in pairs_set:
                    pairs_set.add(new_pair)
            else:
                val[first] = first
                
        return found, pairs_set
            
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
            
        result_set = set()
        nums.sort()
        
        for idx_a, a in enumerate(nums):
            # a must be no bigger than 0
            if a <= 0:
                res = self.twoSum(nums[idx_a+1:], -a)
                found = res[0]
                pairs = res[1]
                if found:
                    for pair in pairs:
                        b, c = pair
                        if (a,b,c) not in result_set:
                            result_set.add((a,b,c))
            else:
                break
            
        return list(result_set)