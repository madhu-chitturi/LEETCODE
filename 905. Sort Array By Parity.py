                                                                    905. Sort Array By Parity
  
  class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        n=len(nums)
        for i in range(n):
            if(nums[i]%2==0):
                a.append(nums[i])
            else:
                b.append(nums[i])
        c=sorted(a)
        d=sorted(b)
        e=c+d
        return e
