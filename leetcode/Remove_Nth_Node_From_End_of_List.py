# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = ListNode(0, head)
        pre, cur = temp, head

        while cur and n:
            cur = cur.next
            n -= 1
        
        while cur:
            cur = cur.next
            pre = pre.next
        pre.next = pre.next.next
        return temp.next

def list_to_linkedlist(lst):
    """Helper function to convert a list to a linked list"""
    dummy = ListNode(0)
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    """Helper function to convert a linked list to a list"""
    result = []
    current = node
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    n = 2
    
    linkedlist_head = list_to_linkedlist(head)
    solution = Solution()
    result = solution.removeNthFromEnd(linkedlist_head, n)
    
    result_list = linkedlist_to_list(result)
    print(result_list)  # Output: [1, 2, 3, 5]
