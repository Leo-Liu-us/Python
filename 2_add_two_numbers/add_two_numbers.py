# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2[:]
        if l2 is None:
            return l1[:]
            
        head1, head2 = l1, l2
        result = None
        carry = 0
        
        #add the common length which equals the shorter linkedlist
        while head1 and head2:
            new_sum = (head1.val + head2.val + carry) % 10
            carry = (head1.val + head2.val + carry)/10
            new_node = ListNode(new_sum)
            
            #mounte the new node to the result list
            if result is None:
                result, new_head = new_node, new_node
            else:
                new_head.next, new_head = new_node, new_node

            #next step
            head1, head2 = head1.next, head2.next
            
        #add the remaining part
        #head1 is None, head2 not None
        #head1 not None, head1 is None
        #Both head1 and head2 are None
        if head1:
            head = head1
        else:
            head = head2
        #
        while head:
            new_sum = (carry + head.val)%10
            carry = (carry + head.val)/10
            new_node = ListNode(new_sum)
            new_head.next, new_head = new_node, new_node
            
            #next step
            head = head.next
        if carry == 1:
            new_head.next = ListNode(carry)
            
        
        return result