class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums=sorted(nums)
        l1=[]
        for i in range(pow(2,n)):
            l=[]
            for j in range(n):
                if((i>>j)&1):
                    l.append(nums[j])
            l1.append(l)
        l2=[]
        for i in range(len(l1)):
            x=l1[i]
            if x not in l2:
                l2.append(x)
        return l2
