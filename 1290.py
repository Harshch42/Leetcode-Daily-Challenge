# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # bin_no = ""

        # while head:
        #     bin_no += str(head.val)
        #     head = head.next

        # res = int(bin_no , 2)

        # return res

        ######## USING ARRAY
        # lst = []

        # while head:
        #     lst.append(head.val)
        #     head = head.next

        # lst = [str(i) for i in lst]

        # return int(''.join(lst) , 2)

        n = 0
        temp = head

        while temp:
            n += 1
            temp = temp.next

        res = 0
        c = 1

        while head:
            res += head.val * (2 ** (n - c))
            c += 1
            head = head.next

        return res
