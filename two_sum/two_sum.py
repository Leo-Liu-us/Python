class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    # assume there is no duplicate element
    def twoSum(self, nums, target):
        tempDict = {}
        for index, item in enumerate(nums):
            difference = target - item
            if difference in tempDict:
                index1 = index + 1
                index2 = tempDict[difference] + 1
                if index1 > index2:
                    return (index2, index1)
                else:
                    return (index1, index2)
            tempDict[item] = index
            