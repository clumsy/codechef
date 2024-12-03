class Solution:
    def detectCycle(self, head):
        slw, fst = head.next, head.next.next
        while slw != fst:
            slw, fst = slw.next, fst.next.next
        if slw is None or fst is None:
            return None
        k, fst = 0, head
        while slw != fst:
            slw, fst = slw.next, fst.next
        res = slw
        return res
