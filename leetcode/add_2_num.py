class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode()
        current = dummy

        while l1 or l2 or carry:
            # Extract values from the current nodes
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate the sum and carry
            _sum = x + y + carry
            carry = _sum // 10

            # Create a new node with the sum % 10
            current.next = ListNode(_sum % 10)
            current = current.next

            # Move to the next nodes in the input lists if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
