# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(0)
        tail = dummyhead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum%10
            carry = sum//10
            newnode = ListNode(digit)
            tail.next = newnode
            tail = tail.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        result = dummyhead.next
        dummyhead.next = None
        return result