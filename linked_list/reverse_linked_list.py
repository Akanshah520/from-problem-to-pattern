class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next   # store next node
        curr.next = prev        # reverse pointer
        prev = curr             # move prev forward
        curr = next_node        # move curr forward

    return prev
