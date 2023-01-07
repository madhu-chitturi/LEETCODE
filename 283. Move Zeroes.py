                                                                283. Move Zeroes
  
  class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        p1=0
        p2=1
        while(p1<n and p2<n):
            if(nums[p1]==0 and nums[p2]!=0):
                tmp=nums[p1]
                nums[p1]=nums[p2]
                nums[p2]=tmp
                p1+=1
                p2+=1
            elif(nums[p1]==0 and nums[p2]==0):
                p2+=1
            else:
                p1+=1
                p2+=1
