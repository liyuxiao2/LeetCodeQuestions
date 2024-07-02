def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        prev = None
        cur = head
        
        
            
        while(cur != None):
            if prev is None and cur.val == val:  # Check for head node removal
                head = cur.next
            elif(cur.val == val):
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head