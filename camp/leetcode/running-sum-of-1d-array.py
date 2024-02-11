class Solution(object):
    def runningSum(self, nums):
        result = [nums[0]]
        for i in range(1, len(nums)):
            result.append(nums[i] + result[i-1])
            
        return result