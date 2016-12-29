# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        print(self.val, ' ')
        if self.next:
            print(self.next)
        return ""

    def set_next(self, next):
        self.next = next


class Solution(object):
        def removeNthFromEnd(self, head, n):
            """
            :type head: ListNode
            :type n: int
            :rtype: ListNode
            """
            size = 0
            ptr = head
            while ptr:
                ptr = ptr.next
                size += 1
            if size == n:
                return head.next
            else:
                count = 0
                ptr = head
                while count < size - n - 1:
                    ptr = ptr.next
                    count += 1
                ptr.next = ptr.next.next
                return head


head = None
while(True):
    x = input("Enter a number\n")
    x = int(x)
    if x == -1:
        break
    if not head:
        head = ListNode(x)
        ptr = head
    else:
        ptr.next = ListNode(x)
        ptr = ptr.next
sln = Solution()
node = sln.removeNthFromEnd(head, 1)
print(node)
