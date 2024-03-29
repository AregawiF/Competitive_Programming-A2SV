class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        zeros = 0
        ans = 0
        while right < len(nums):
            # if nums[right] == 1:
            #     right += 1
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            ans = max(ans, (right - left))
            right += 1
        return ans