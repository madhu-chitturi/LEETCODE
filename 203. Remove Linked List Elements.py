                                                            203. Remove Linked List Elements
  
  class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        tmp=head
        if(head==None):
            return head
        if(head.val==val and head.next==None):
            return 
        while(head!=None and head.next!=None):
            if(head.next.val==val):
                head.next=head.next.next
            else:
                head=head.next
            if(tmp.val==val):
                tmp=tmp.next
        return tmp
