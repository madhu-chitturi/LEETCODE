                                                          1. Two Sum
  Link:https://leetcode.com/problems/two-sum/description/
    
  class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if(nums[i]+nums[j]==target):
                    return [i,j]
