

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n=len(nums)
        b=[]
        c=[]
        for i in range(n):
            if(nums[i]%2==0):
                b.append(nums[i])
            else:
                c.append(nums[i])
        d=[]
        for i in range(n//2):
            d.append(b[i])
            d.append(c[i])
        return d
