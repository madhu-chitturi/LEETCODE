                                                                       136. Single Number
  
  class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums1=sorted(nums)
        if(n==1):
            return nums1[0]
        else:
            if(nums1[0]!=nums1[1]):
                return nums1[0]
            elif(nums1[n-1]!=nums1[n-2]):
                return nums1[n-1]
            else:
                for i in range(1,n-1):
                    if(nums1[i-1]!=nums1[i] and nums1[i]!=nums1[i+1]):
                        return nums1[i]
     
