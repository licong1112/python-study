class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(head):
    runner = head
    while runner is not None:
        print runner.val,
        runner = runner.next


def to_node_list(val_list):
    if not val_list:
        return None

    head = ListNode(val_list[0])
    runner = head
    for val in val_list[1:]:
        new_node = ListNode(val)
        runner.next = new_node
        runner = runner.next

    return head


def remove_nth_from_end(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    if n == 0:
        return head

    fake_head = ListNode(0)
    fake_head.next = head

    pre = fake_head
    curr = head
    end = head

    while n > 1:
        end = end.next
        n -= 1

    while end.next != None:
        pre = pre.next
        curr = curr.next
        end = end.next

    pre.next = curr.next
    curr.next = None

    return fake_head.next



if __name__ == "__main__":
    input_vals = map(int, raw_input().split())
    n = int(raw_input())
    result = remove_nth_from_end(to_node_list(input_vals), n)
    print_list(result)
