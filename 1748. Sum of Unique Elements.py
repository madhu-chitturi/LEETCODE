class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        l=[0]
        for i in range(len(nums)):
            a=nums.count(nums[i])
            if(a==1):
                l.append(nums[i])
        return sum(l)
