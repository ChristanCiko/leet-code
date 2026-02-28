# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        # 设置一个指针
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)  # 空间复杂度为O(n)
            current_node = current_node.next

        return vals == vals[::-1]
