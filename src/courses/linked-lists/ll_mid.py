def getMiddleElement(head):
    slw = fst = head
    while fst and fst.next:
        slw, fst = slw.next, fst.next.next
    res = slw.data
    return res
