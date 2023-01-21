
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[]
        for i in range(n):
            b=pow(nums[i],2)
            a.append(b)
        c=sorted(a)
        return c
