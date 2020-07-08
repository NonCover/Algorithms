"""
链表的归并排序
时间复杂度：O（nlogn）
非递归法
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, root: ListNode) -> ListNode:
        n = self.getListLength(root)
        lvl = 1
        head = ListNode(-1)
        head.next = root
        while lvl < n:
            node = head
            k = 0
            while k + lvl < n:
                p1 = node.next
                p2 = p1
                for _ in range(lvl): p2 = p2.next
                i, j = 0, 0
                while i < lvl and j < lvl and p2:
                    if p1.val < p2.val:
                        i += 1
                        node.next = p1
                        p1 = p1.next
                    else:
                        j  += 1
                        node.next = p2
                        p2 = p2.next
                    node = node.next
                while i < lvl:
                    i += 1
                    node.next = p1
                    p1 = p1.next
                    node = node.next
                while j < lvl and p2:
                    j += 1
                    node.next = p2
                    p2 = p2.next
                    node = node.next
                node.next = p2
                k += (2 * lvl)
            lvl *= 2
        return head.next

    def getListLength(self, root: ListNode) -> int:
        n = 0
        while root:
            root, n = root.next, n + 1
        return n


from typing import List
def arr2List(arr: List) -> ListNode:
    n = len(arr)
    root = ListNode(-1)
    if n > 0:
        head = root
        for i in range(n):
            head.next = ListNode(arr[i])
            head = head.next
    return root.next

def printList(root: ListNode) -> None:
    arr = []
    while root:
        arr.append(root.val)
        root = root.next
    print(arr)

if __name__ == '__main__':
    arr = [8,6,4,2,7,0]
    root = arr2List(arr)
    out = Solution().sortList(root)
    printList(out)