                                                    19. Remove Nth Node From End of List                  
  Link:https://leetcode.com/problems/remove-nth-node-from-end-of-list/
      
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def length(head):
    cnt=0
    while(head!=None):
        cnt+=1
        head=head.next
    return cnt
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp=head
        a=length(head)
        b=a-n
        if(b==0):
            return head.next 
        for i in range(b-1):
            head=head.next
        head.next=head.next.next
        return tmp
