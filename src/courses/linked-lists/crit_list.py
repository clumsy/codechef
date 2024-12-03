def solve(head):
    res = 0
    prv, cur, nxt = head, head.next if head else None, head.next.next if head and head.next else None
    while nxt:
        lft, rgt = cur.val - prv.val, cur.val - nxt.val
        res += (lft > 0 and rgt > 0) or (lft < 0 and rgt < 0)
        prv, cur, nxt = cur, nxt, nxt.next
    return res
