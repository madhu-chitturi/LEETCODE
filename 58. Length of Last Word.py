                                                                  58. Length of Last Word               
  
  class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=list(s.split())
        n=len(a)
        b=list(a[n-1])
        return len(b)
