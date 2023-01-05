                                                                33. Search in Rotated Sorted Array
  
  LINK:https://leetcode.com/problems/search-in-rotated-sorted-array/
      
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            x=nums.index(target)
            return x   
        else:
            return -1
