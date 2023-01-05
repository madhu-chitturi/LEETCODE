                                                                      27. Remove Element    
  LINK:https://leetcode.com/problems/remove-element
  
  class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        i=0
        while(i<n):
            if(nums[i]==val):
                nums.pop(i)
                
                n=n-1
            else:
                i+=1
