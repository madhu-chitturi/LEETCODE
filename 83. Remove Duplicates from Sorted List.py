                                                              83. Remove Duplicates from Sorted List
  
  class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp=head
        while(head!=None and head.next!=None):
            if(head.val==head.next.val):
                head.next=head.next.next
            else:
                head=head.next
        return tmp
