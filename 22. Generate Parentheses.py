                                                            22. Generate Parentheses
  
  def printp(l1,n,oc,cc,idx,l):
    if(idx==n):
        s=''
        for d in l1:
            s+=d
        l.append(s)
    if(oc<n//2):
        l1[idx]='('
        printp(l1,n,oc+1,cc,idx+1,l)
    if(oc>cc):
        l1[idx]=')'
        printp(l1,n,oc,cc+1,idx+1,l)
  
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        n=n*2
        l=[]
        l1=[0 for i in range(n)]
        s=''
        printp(l1,n,0,0,0,l)
        return l
        
