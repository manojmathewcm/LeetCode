# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        total_head = None
        ll_list = [l1,l2]
        while ll_list:
            digTot = carry
            for elem in ll_list:
                digTot += elem.val
            if digTot > 9:
                carry = 1
                digTot -= 10
            else:
                carry = 0
            if total_head == None:
                total_head = ListNode(val=digTot)
                prev_tot_node = total_head
            else:
                curr_tot_node = ListNode(val=digTot)
                prev_tot_node.next = curr_tot_node
                prev_tot_node = curr_tot_node
            ll_list = [elem.next for elem in ll_list if elem.next != None]
        if carry:
            curr_tot_node = ListNode(val=carry)
            prev_tot_node.next = curr_tot_node

        return total_head

