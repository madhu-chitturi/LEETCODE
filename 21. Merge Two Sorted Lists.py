                                                          21. Merge Two Sorted Lists
  LINK:https://leetcode.com/problems/merge-two-sorted-lists/
      
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1=list1
        p2=list2
        if(p1==None):
            return p2
        if(p2==None):
            return p1
        

        nn=ListNode(-1)
        tmp=nn
        while(p1!=None and p2!=None):
            if(p1.val<=p2.val):
                nn.next=p1
                p1=p1.next
            else:
                nn.next=p2
                p2=p2.next
            nn=nn.next
        if(p1!=None):
            nn.next=p1
        else:
            nn.next=p2
        return tmp.next
