class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        l1=[]
        for i in range(pow(2,n)):
            l=[]
            for j in range(n):
                if((i>>j)&1):
                    l.append(nums[j])
            l1.append(l)
        return l1
