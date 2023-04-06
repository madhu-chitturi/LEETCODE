class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a=heights
        c=sorted(a)
        cnt=0
        for i in range(len(a)):
            if(a[i]!=c[i]):
                cnt+=1
        return cnt
