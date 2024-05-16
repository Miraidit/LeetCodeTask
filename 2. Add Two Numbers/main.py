# my solution

l1 = l1[::-1]
l2 = l2[::-1]
l1_n = int(''.join(map(str, l1)))
l2_n = int(''.join(map(str, l2)))
sum = l1_n + l2_n
sum = str(sum)
a = []
for i in sum :
    a.append(int(i))
a = a[::-1]
print(a)

#solution that worked
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0) 
        current = dummy_head
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry, digit = divmod(total, 10)
            current.next = ListNode(digit)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next