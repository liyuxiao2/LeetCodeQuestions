def oddEvenList(head):
  """
  Rearranges a linked list such that odd-positioned nodes are followed by even-positioned nodes.

  Args:
      head (ListNode): The head of the linked list.

  Returns:
      ListNode: The head of the rearranged linked list.
  """
  if not head:
    return head

  # Initialize odd and even pointers
  odd = head
  even = head.next
  even_head = even  # Store the head of the even nodes

  # Loop while even and even.next are not None
  while even and even.next:
    odd.next = even.next  # Link odd node to the next odd node
    even.next = even.next.next  # Link even node to the next even node
    odd = odd.next  # Move odd pointer forward
    even = even.next  # Move even pointer forward

  # Connect the tail of the odd list to the head of the even list
  odd.next = even_head

  return head