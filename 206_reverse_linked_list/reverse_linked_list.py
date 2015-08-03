# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        else:
            #starts from the second node
            old_list = head.next
            head.next = None
            
            while old_list is not None:
                tmp = old_list.next
                old_list.next = head
                head = old_list
                old_list = tmp
                
            return head