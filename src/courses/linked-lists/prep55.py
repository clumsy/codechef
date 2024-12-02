class Solution:
    def removeDuplicates(self, head):
        unq = {head.data}
        cur = head
        while cur.next:
            if cur.next.data in unq:
                cur.next = cur.next.next
            else:
                unq.add(cur.next.data)
                cur = cur.next
        return head
