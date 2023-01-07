                                                                169. Majority Element
  
  class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        b=list(set(nums))
        for i in range(len(b)):
            a=nums.count(b[i])
            if(a>len(nums)//2):
                return b[i]
