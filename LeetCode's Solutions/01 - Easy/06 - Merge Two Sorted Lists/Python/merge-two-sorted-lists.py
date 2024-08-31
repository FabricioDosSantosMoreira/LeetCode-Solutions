from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode(val={self.val}, next={self.next})"


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # NOTE: Time Complexity = O(m + n)
        # 'm' is the length of 'list1'
        # 'n' is the length of 'list2'
        dummy = ListNode() 
        tail = dummy 

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1 
                list1 = list1.next 
            else:
                tail.next = list2 
                list2 = list2.next  
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


solution = Solution()


list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))
answer = solution.mergeTwoLists(list1=list1, list2=list2)
print(f"return: {answer}")


list1 = ListNode()
list2 = ListNode()
answer = solution.mergeTwoLists(list1=list1, list2=list2)
print(f"return: {answer}")


list1 = ListNode()
list2 = ListNode(val=0)
answer = solution.mergeTwoLists(list1=list1, list2=list2)
print(f"return: {answer}")
