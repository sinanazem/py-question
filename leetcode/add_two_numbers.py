# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        val = l1.val + l2.val
        res = ListNode(val % 10)
        carry = val // 10

        temp = res
        l1, l2 = l1.next, l2.next

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2  else 0
            val = v1 + v2 + carry
            temp.next = ListNode(val % 10)
            temp = temp.next
            carry = val // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         carry = 0
#         dummy = ListNode()
#         current = dummy

#         while l1 or l2 or carry:
#             # Extract values from the current nodes
#             x = l1.val if l1 else 0
#             y = l2.val if l2 else 0

#             # Calculate the sum and carry
#             _sum = x + y + carry
#             carry = _sum // 10

#             # Create a new node with the sum % 10
#             current.next = ListNode(_sum % 10)
#             current = current.next

#             # Move to the next nodes in the input lists if available
#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next

#         return dummy.next
