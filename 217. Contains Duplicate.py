class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x=len(nums)
        y=set(nums)
        b=len(y)
        return b<=x-1
