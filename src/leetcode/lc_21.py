# Definition for singly-linked list.


class ListNode:
    def __init__(
        self: "ListNode",
        val: int = 0,
        next: "None | ListNode" = None,
    ) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: ListNode | None,
        list2: ListNode | None,
    ) -> ListNode | None:
        if not list1 or not list2:
            return list1 or list2

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)

            return list1

        list2.next = self.mergeTwoLists(list2.next, list1)

        return list2
