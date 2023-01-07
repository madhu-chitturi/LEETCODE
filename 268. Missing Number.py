                                                              268. Missing Number
  
  class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max1=max(nums)
        if(max1==len(nums)):
            for i in range(len(nums)):
                if i not in nums:
                    return i
        else:
            for i in range(len(nums)+1):
                if i not in nums:
                    return i
