class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l=[]
        while(head!=None):
            l.append(str(head.val))
            head=head.next
        a=l[0]
        for i in range(1,len(l)):
            a+=l[i]
        b=int(a,2)
        return b
