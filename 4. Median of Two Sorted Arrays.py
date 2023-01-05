                                                                  4. Median of Two Sorted Arrays
  Link:https://leetcode.com/problems/median-of-two-sorted-arrays
      
  class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=nums1+nums2
        m=sorted(n)
        x=len(m)
        mid=(x-1)//2
        if(x%2!=0):
            median=m[mid]
        else:
            median=(m[mid]+m[mid+1])/2
        return median
        
