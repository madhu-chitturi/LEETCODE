class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l=[]
        for i in range(len(accounts)):
            l.append(sum(accounts[i]))
        a=max(l)
        return a
        
