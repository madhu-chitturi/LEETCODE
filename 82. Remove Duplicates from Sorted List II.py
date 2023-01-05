                                                        82. Remove Duplicates from Sorted List II                         
  
  
  class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        while(head!=None):
            l.append(head.val)
            head=head.next
        a=list(set(l))
        c=[]
        for i in range(len(a)):
            b=l.count(a[i])
            if(b==1):
                c.append(a[i])
        d=sorted(c)
        nn=ListNode(-1)
        tmp=nn
        for i in range(len(d)):
            n=ListNode(d[i])
            nn.next=n
            nn=nn.next
        return tmp.next
