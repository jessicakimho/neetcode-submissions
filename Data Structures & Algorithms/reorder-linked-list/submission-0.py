# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next # slow is now at the midpoint
        
        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        second = curr
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second 
            second.next = temp1
            first, second = temp1, temp2
        
