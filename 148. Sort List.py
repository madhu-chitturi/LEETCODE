                                                                            148. Sort List
  
  class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        while(head!=None):
            l.append(head.val)
            head=head.next
        n=ListNode(-1)
        tmp=n
        l=sorted(l)
        for i in range(len(l)):
            nn=ListNode(l[i])
            n.next=nn
            n=n.next
        return tmp.next
