                                                                      206. Reverse Linked List
  
  class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        while(head!=None):
            tmp=head.next
            head.next=prev
            prev=head
            head=tmp
        return prev
