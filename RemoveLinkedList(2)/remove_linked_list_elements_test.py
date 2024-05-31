import unittest
from list_node import ListNode
from remove_linked_list_elements import Solution

class TestRemoveNodesWithCount(unittest.TestCase):
  # Helper function to create a linked list from a list of values
  def create_linked_list(self, values):
    head = None
    prev = None
    for value in values:
      node = ListNode(value)
      if not head:
        head = node
      if prev:
        prev.next = node
      prev = node
    return head

  def test_empty_list(self):
    # Empty list, no change expected
    target_counts = []
    head = None
    result = Solution().remove_nodes_with_count(head, target_counts)  # Don't pass head as argument to constructor
    self.assertEqual(result, None)  # Expect None for empty list

  def test_remove_all_counts(self):
    # Remove all occurrences of a value
    target_counts = [(7, 2), (6, 6)]
    values = [7, 7, 5, 4, 3, 5, 6, 7, 6, 6, 6, 6, 6]
    expected_list = [5, 4, 3, 5, 7]
    head = self.create_linked_list(values)
    result = Solution().remove_nodes_with_count(head, target_counts)  # Don't pass head as argument to constructor
    self.assertEqual(self.convert_linked_list_to_array(result), expected_list)

  def test_remove_some_counts(self):
    # Remove specific counts
    target_counts = [(7, 1), (6, 4), (5, 2)]
    values = [7, 7, 5, 4, 3, 5, 6, 7, 6, 6, 6, 6, 6]
    expected_list = [7, 4, 3, 7, 6, 6]
    head = self.create_linked_list(values)
    result = Solution().remove_nodes_with_count(head, target_counts)  # Don't pass head as argument to constructor
    self.assertEqual(self.convert_linked_list_to_array(result), expected_list)

  def test_remove_zero_count(self):
    # Remove zero count shouldn't affect the list
    target_counts = [(7, 0), (6, 2), (5, 1)]
    values = [7, 7, 5, 4, 3, 5, 6, 7, 6, 6, 6, 6, 6]
    expected_list = [7, 7, 4, 3, 5, 7, 6, 6, 6, 6]  # No change for 7 (count 0)
    head = self.create_linked_list(values)
    result = Solution().remove_nodes_with_count(head, target_counts)  # Don't pass head as argument to constructor
    self.assertEqual(self.convert_linked_list_to_array(result), expected_list)

  def test_remove_out_of_bounds_count(self):
    # Try removing more than existing nodes
    target_counts = [(7, 3), (6, 10), (5, 2)]
    values = [7, 7, 5, 4, 3, 5, 6, 7, 6, 6, 6, 6, 6]
    expected_list = [4, 3]  # Remove at most the existing count
    head = self.create_linked_list(values)
    result = Solution().remove_nodes_with_count(head, target_counts)  # Don't pass head as argument to constructor
    self.assertEqual(self.convert_linked_list_to_array(result), expected_list)

  # Add more test cases for edge cases

  
  def convert_linked_list_to_array(self, head):
    """
    Converts a linked list to a list of node values.

    Args:
        head: The head node of the linked list.

    Returns:
        A list containing the values of all nodes in the linked list.
    """

    result_values = []
    current = head
    while current:
      result_values.append(current.val)
      current = current.next
    return result_values
  
  
  
