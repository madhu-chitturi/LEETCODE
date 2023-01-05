                                                                      66. Plus One                      
  
  class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        y=str(digits[0])
        for i in range(1,len(digits)):
            x=str(digits[i])
            y+=x
        a=int(y)+1
        b=list(map(int,str(a)))
        return b
