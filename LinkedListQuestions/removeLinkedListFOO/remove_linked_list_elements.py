from listnode import ListNode  # Import ListNode class (assuming it's in a separate file)
class Solution:
    def remove_nodes_with_count(self, head, target_counts):
        """
        Removes nodes from the linked list based on target values and desired removal counts.

        Args:
            head: The head node of the linked list.
            target_counts: A list of tuples where each tuple represents a target value and its desired removal count.

        Returns:
            The modified head node of the linked list.
        """
        
        #creates a dictionary storing key, value pairs
        target_dict = dict(target_counts)
        
        # Dummy node to handle edge cases easily
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head

        while cur != None:
            if cur.val in target_dict:
                if target_dict[cur.val] > 0:
                    target_dict[cur.val] -= 1
                    prev.next = cur.next  # Remove the node
                else:
                    prev = cur  # Move to the next node
            else:
                prev = cur  # Move to the next node
            cur = cur.next

        return dummy.next